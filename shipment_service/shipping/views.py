from django.shortcuts import get_object_or_404, render, redirect
from bson import ObjectId
from django.db import connection

# Create your views here.
from .models import Product
from .models import POS, Shipment
from .forms import ShipmentForm, ShipmentEditForm
from django.utils import timezone
from django.http import Http404
import json
from django.urls import reverse


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def purchase_order_list(request):
    # Retrieve all purchase orders from the POS collection
    purchase_orders = POS.objects.all()
    
    # Pass the purchase orders to the template for rendering
    return render(request, 'purchase_order_list.html', {'purchase_orders': purchase_orders})


def shipment_list(request):
    # Retrieve all purchase orders from the POS collection
    shipments = Shipment.objects.all()
    
    # Pass the purchase orders to the template for rendering
    return render(request, 'shipment_list.html', {'shipments': shipments})


def purchase_order_detail(request, pk):
    purchase_order = POS.objects.get(pk=ObjectId(pk))
    shipments = Shipment.objects.all() if purchase_order.status == POS.READY_FOR_SHIPMENT else None
    # print(purchase_order.shipment.id)
    return render(request, 'purchase_order_detail.html', {'purchase_order': purchase_order, 'shipments': shipments})



def shipment_status(request, pk):
    # Retrieve the shipment object
    shipment = Shipment.objects.get(pk=ObjectId(pk))

    # Retrieve purchase order IDs from the shipment's JSON field
    po_ids = shipment.purchase_orders

    # Retrieve purchase orders related to the shipment
    purchase_orders = POS.objects.filter(id__in=po_ids)

    # Add logic to handle the shipment status
    context = {
        'shipment': shipment,
        'purchase_orders': purchase_orders,
    }
    return render(request, 'shipment_status.html', context)








def add_purchase_order_to_shipment(request):
    if request.method == 'POST':
        # Retrieve purchase order ID from the form data
        purchase_order_id = request.POST.get('purchase_order_id')

        # Retrieve the shipment ID from the form data and convert it to an integer
        shipment_id = request.POST.get('shipment')
        shipment_id = int(shipment_id) if shipment_id else None

        try:
            # Retrieve the existing shipment or create a new one if the ID is not provided
            if shipment_id:
                shipment = Shipment.objects.get(pk=shipment_id)
            else:
                shipment = Shipment.objects.create(confirmedOn=timezone.now())
        except Shipment.DoesNotExist:
            raise Http404("Shipment does not exist")  # Handle non-existent shipment here
        
        # Retrieve the purchase order using the ID
        purchase_order = get_object_or_404(POS, pk=purchase_order_id)

        # Check if the purchase order is ready for shipment
        if purchase_order.status == POS.READY_FOR_SHIPMENT:
            # Associate the purchase order with the shipment
            purchase_order.shipment = shipment
            purchase_order.status = POS.ADDED_TO_SHIPMENT
            purchase_order.save()

        # Redirect to the purchase order detail page
        return redirect('purchase_order_detail', pk=purchase_order_id)
    
    shipments = Shipment.objects.all()
    return render(request, 'purchase_order_detail.html', {'purchase_order': purchase_order, 'shipments': shipments})



def create_shipment(request):
    if request.method == 'POST':
        # Retrieve the destination from the form
        destination = request.POST.get('destination')
        
        # Retrieve the selected purchase order IDs from the form
        purchase_order_ids = request.POST.getlist('purchase_order_ids')
        
        # Create a new list to store the purchase order IDs as ObjectId instances
        po_ids = []
        
        # Convert the list of purchase order IDs to ObjectId instances
        po_ids = [ObjectId(p_id) for p_id in purchase_order_ids] if purchase_order_ids else []

        print(purchase_order_ids)
        new_shipment = Shipment.objects.create(destination=destination, confirmedOn=timezone.now(), purchase_orders=po_ids)
        
        # Associate the selected purchase orders with the new shipment
        if po_ids:
            purchase_orders = POS.objects.filter(id__in=po_ids)
            for purchase_order in purchase_orders:
                purchase_order.shipment = new_shipment
                purchase_order.status = POS.ADDED_TO_SHIPMENT
                purchase_order.save()
        
        
        
        # Redirect to the shipment status page for the newly created shipment
        return redirect('shipment_status', pk=new_shipment.pk)
    
    # If it's a GET request, render the form to create a new shipment
    purchase_orders = POS.objects.filter(status=POS.READY_FOR_SHIPMENT)
    return render(request, 'create_shipment.html', {'purchase_orders': purchase_orders})


def edit_shipment(request, pk):
    shipment = get_object_or_404(Shipment, pk=ObjectId(pk))
    
    if request.method == 'POST':
        form = ShipmentEditForm(request.POST, instance=shipment)
        if form.is_valid():
            form.save()
            return redirect('shipment_status', pk=ObjectId(pk))
    else:
        form = ShipmentEditForm(instance=shipment)
    
    return render(request, 'edit_shipment.html', {'form': form})


def remove_purchase_order(request, shipment_id):
    if request.method == 'POST':
        # Retrieve the purchase order ID from the form data
        purchase_order_id = request.POST.get('purchase_order_id')
        purchase_order_id = ObjectId(purchase_order_id)

        # Get the shipment object
        shipment = get_object_or_404(Shipment, pk=ObjectId(shipment_id))

        # Get the purchase order object
        purchase_order = get_object_or_404(POS, pk=purchase_order_id)

        # Check if the purchase order is associated with the shipment
        if purchase_order_id not in shipment.purchase_orders:
            return render(request, 'error.html', {'message': 'Purchase order is not associated with the shipment'})


        # Change the status of the purchase order to "Ready for Shipment"
        purchase_order.status = POS.READY_FOR_SHIPMENT
        purchase_order.save()

        # Remove the association with the shipment
        purchase_order.shipment = None
        purchase_order.save()

        shipment.purchase_orders.remove(purchase_order_id)
        shipment.save()

        # Redirect back to the shipment status page
        return redirect(reverse('shipment_status', args=[shipment_id]))

    # If the request method is not POST, render an error page or handle it accordingly
    return render(request, 'error.html', {'message': 'Invalid request method'})



def confirm_shipment(request, shipment_id):
    # Retrieve the shipment object
    shipment = get_object_or_404(Shipment, pk=shipment_id)

    if request.method == 'POST':
        # Set the confirmedOn field to the current datetime
        shipment.confirmedOn = timezone.now()
        shipment.save()

        # Redirect back to the shipment status page
        return redirect('shipment_status', pk=shipment_id)
    
    po_ids = shipment.purchase_orders

    # Retrieve purchase orders related to the shipment
    purchase_orders = POS.objects.filter(id__in=po_ids)

    # Add logic to handle the shipment status
    context = {
        'shipment': shipment,
        'purchase_orders': purchase_orders,
        }
    # If it's a GET request, render a confirmation page
    return render(request, 'shipment_status.html', context)