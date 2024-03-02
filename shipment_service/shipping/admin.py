from django.contrib import admin
from .models import Product, Shipment, POS

# Register your models here.


# Define the admin class for Product
class ProductAdmin(admin.ModelAdmin):
    pass  # No need to specify list_display or list_display_links for displaying all fields

# Define the admin class for Shipment
class ShipmentAdmin(admin.ModelAdmin):
    pass  # No need to specify list_display or list_display_links for displaying all fields

# Define the admin class for POS
class POSAdmin(admin.ModelAdmin):
    pass  # No need to specify list_display or list_display_links for displaying all fields

# Register the models with the admin classes
admin.site.register(Product, ProductAdmin)
admin.site.register(Shipment, ShipmentAdmin)
admin.site.register(POS, POSAdmin)
