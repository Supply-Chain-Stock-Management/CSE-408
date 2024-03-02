from django.urls import path

from . import views

urlpatterns = [
    path('purchase-orders/<str:pk>/', views.purchase_order_detail, name='purchase_order_detail'),
    path('purchase-orders/', views.purchase_order_list, name='purchase_order_list'),
    path('add_purchase_order/', views.add_purchase_order_to_shipment, name='add_purchase_order'),
    path('shipments/<str:pk>/', views.shipment_status, name='shipment_status'),
    path('shipments/', views.shipment_list, name='shipment_list'),
    path('create/', views.create_shipment, name='create_shipment'),
    path('products/', views.product_list, name='product_list'),
    path('shipments/<str:pk>/edit/', views.edit_shipment, name='shipment_edit'),
    path('shipments/<str:shipment_id>/remove_order/', views.remove_purchase_order, name='remove_purchase_order'),
    path('shipments/<str:pk>/confirm/', views.confirm_shipment, name='shipment_confirm'),
]
