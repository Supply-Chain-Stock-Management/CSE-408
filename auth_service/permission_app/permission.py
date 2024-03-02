from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

# Define custom permissions
CAN_ASSIGN_PERMISSION = 'permission_app.can_assign_permission'
CAN_VIEW_PRODUCT = 'permission_app.can_view_product'
CAN_DELETE_USER = 'permission_app.can_delete_user'
CAN_CONFIRM_SUPPLY = 'permission_app.can_confirm_supply'
CAN_PURCHASE = 'permission_app.can_purchase'
CAN_CREATE_PRODUCT = 'permission_app.can_create_product'
CAN_VIEW_SHIPMENT = 'permission_app.can_view_shipment'
CAN_TRACK_TRANSPORT = 'permission_app.can_track_transport'
CAN_MODIFY_PRODUCT = 'permission_app.can_modify_product'
CAN_MANAGE_ORDERS = 'permission_app.can_manage_orders'
CAN_VIEW_PENDING_REQUESTS = 'permission_app.can_view_pending_requests'
CAN_REMOVE_USER = 'permission_app.can_remove_user'
CAN_ASSIGN_TO_GROUP = 'permission_app.can_assign_to_group'

def create_custom_permissions():

    # Define custom permissions with their human-readable names
    custom_permissions = [
        (CAN_ASSIGN_PERMISSION, 'Can assign permission'),
        (CAN_VIEW_PRODUCT, 'Can view product'),
        (CAN_DELETE_USER, 'Can delete user'),
        (CAN_CONFIRM_SUPPLY, 'Can confirm supply'),
        (CAN_PURCHASE, 'Can purchase'),
        (CAN_CREATE_PRODUCT, 'Can create product'),
        (CAN_VIEW_SHIPMENT, 'Can view shipment'),
        (CAN_TRACK_TRANSPORT, 'Can track transport'),
        (CAN_MODIFY_PRODUCT, 'Can modify product'),
        (CAN_MANAGE_ORDERS, 'Can manage orders'),
        (CAN_VIEW_PENDING_REQUESTS, 'Can view pending requests'),
        (CAN_REMOVE_USER, 'Can remove user'),
        (CAN_ASSIGN_TO_GROUP, 'Can assign to group'),
        # Add more custom permissions as needed
    ]

    # for codename, name in custom_permissions:
    #     Permission.objects.get_or_create(
    #         codename=codename,
    #         name=name,
    #         content_type=None
    #     )

    print("Custom permissions created successfully.")

# Call the function to create custom permissions
create_custom_permissions()
