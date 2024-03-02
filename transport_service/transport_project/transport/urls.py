from django.urls import path
from . import views

urlpatterns = [
    path('shipments/', views.shipment_list, name='shipment_list'),
    path('vehicles/', views.vehicle_list, name='vehicle_list'),
    path('vehicles/<int:vehicle_id>/', views.vehicle_details, name='vehicle_details'),
    path('vehicles/<int:vehicle_id>/assign_shipment/', views.shipment_to_vehicle, name='assign_shipment'),

    path('vehicles/create', views.create_vehicle, name='create_vehicle'),
]
