from django.shortcuts import render, redirect
from .models import Shipment, Vehicle
from .forms import VehicleForm
from django.shortcuts import render, get_object_or_404

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
    return render(request, 'vehicle_details.html', {'vehicle': vehicle})





def shipment_to_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
    
    if request.method == 'POST':
        selected_shipments_ids = request.POST.getlist('shipments')
        selected_shipments = Shipment.objects.filter(pk__in=selected_shipments_ids)
        
        total_capacity = sum(selected_shipment.capacity for selected_shipment in selected_shipments)
        
        # Calculate the total weight of already assigned shipments
        assigned_shipments_weight = sum(shipment.capacity for shipment in vehicle.shipments.all())
        
        # Calculate the total weight after assigning new shipments
        total_weight_after_assignment = assigned_shipments_weight + total_capacity
        
        if total_weight_after_assignment <= vehicle.capacity:
            # Update shipment status to "on route" and assign shipments to the vehicle
            for selected_shipment in selected_shipments:
                selected_shipment.status = "on route"
                selected_shipment.vehicle = vehicle
                selected_shipment.save()
            
            return redirect('vehicle_details')  # Redirect to vehicle details page after assigning
        else:
            # If total weight exceeds the vehicle's maximum capacity, render the form again with an error message
            error_message = "Total capacity exceeds the maximum capacity of the vehicle."
            shipments = Shipment.objects.all()  # You might want to pass shipments again to the template
            return render(request, 'assign_shipment_to_vehicle.html', {'error_message': error_message, 'shipments': shipments})
    else:
        # If it's a GET request, render the form with all available shipments
        shipments = Shipment.objects.all()
        return render(request, 'assign_shipment_to_vehicle.html', {'vehicle': vehicle, 'shipments': shipments})

