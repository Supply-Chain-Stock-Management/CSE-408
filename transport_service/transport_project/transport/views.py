from django.shortcuts import render, redirect
from .models import Shipment, Vehicle
from .forms import VehicleForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.
def shipment_list(request):
    shipments = Shipment.objects.all()
    return render(request, 'shipment_list.html', {'shipments': shipments})

def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'vehicle_list.html', {'vehicles': vehicles})


def create_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')  # Redirect to the vehicle list page
    else:
        form = VehicleForm()
    return render(request, 'create_vehicle.html', {'form': form})


def vehicle_details(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
    shipments = Shipment.objects.filter(vehicle=vehicle)
    return render(request, 'vehicle_details.html', {'vehicle': vehicle, 'shipments': shipments})






def shipment_to_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
    
    if request.method == 'POST':
        selected_shipments_ids = request.POST.getlist('shipments')
        selected_shipments = Shipment.objects.filter(pk__in=selected_shipments_ids)
        
        total_weight = sum(selected_shipment.weight for selected_shipment in selected_shipments)
        
        # Calculate the total weight of already assigned shipments
        assigned_shipments_weight = sum(shipment.weight for shipment in Shipment.objects.filter(vehicle=vehicle))
        
        # Calculate the total weight after assigning new shipments
        total_weight_after_assignment = assigned_shipments_weight + total_weight
        
        if total_weight_after_assignment <= vehicle.capacity:
            # Update shipment status to "on route" and assign shipments to the vehicle
            for selected_shipment in selected_shipments:
                selected_shipment.status = "assigned"
                selected_shipment.vehicle = vehicle
                selected_shipment.save()
            
            return redirect('vehicle_details', vehicle_id=vehicle_id)
        else:
            # If total weight exceeds the vehicle's maximum capacity, render the form again with an error message
            error_message = "Total weight exceeds the maximum capacity of the vehicle."
            shipments = Shipment.objects.filter(vehicle=None)  # Get shipments not assigned to any vehicle
            return render(request, 'assign_shipment_to_vehicle.html', {'error_message': error_message, 'shipments': shipments, 'vehicle': vehicle})
    else:
        # If it's a GET request, render the form with all available shipments
        shipments = Shipment.objects.filter(vehicle=None)  # Get shipments not assigned to any vehicle
        return render(request, 'assign_shipment_to_vehicle.html', {'vehicle': vehicle, 'shipments': shipments})




def remove_shipment(request, vehicle_id):
    if request.method == 'POST':
        shipment_id = request.POST.get('shipment_id')
        shipment = get_object_or_404(Shipment, pk=shipment_id)
        
        # Check if the shipment is associated with the correct vehicle
        if shipment.vehicle_id == vehicle_id:
            # Remove the association with the vehicle by setting the vehicle foreign key to None
            shipment.vehicle = None
            shipment.status = "in shipment"
            shipment.save()
            return redirect('vehicle_details', vehicle_id=vehicle_id)  # Redirect to vehicle details page
        else:
            return HttpResponse("Shipment is not associated with the specified vehicle.")
    else:
        return HttpResponse("Method not allowed")
    

def confirm_shipments(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
    shipments = Shipment.objects.filter(vehicle=vehicle, status='on route')

    # Your confirmation logic goes here
    # For example, you might want to update the status of shipments to 'confirmed'
    for shipment in shipments:
        shipment.status = 'en route'
        shipment.save()
    vehicle.status = 'en route'
    vehicle.save()

    # Redirect to the vehicle details page after confirming shipments
    return redirect('vehicle_details', vehicle_id=vehicle_id)