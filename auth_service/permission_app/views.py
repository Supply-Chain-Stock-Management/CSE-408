from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import permission_required


# from permission import (
#     CAN_ASSIGN_PERMISSION,
#     CAN_VIEW_PRODUCT,
#     CAN_DELETE_USER,
#     CAN_CONFIRM_SUPPLY,
#     CAN_PURCHASE,
#     CAN_CREATE_PRODUCT,
#     CAN_VIEW_SHIPMENT,
#     CAN_TRACK_TRANSPORT,
#     CAN_MODIFY_PRODUCT,
#     CAN_MANAGE_ORDERS,
#     CAN_VIEW_PENDING_REQUESTS,
#     CAN_REMOVE_USER,
#     CAN_ASSIGN_TO_GROUP
# )



def role_list_view(request):
    groups = Group.objects.all()
    data = [{'id': group.id, 'name': group.name} for group in groups]
    return JsonResponse(data)

def role_detail_view(request, pk):
    group = get_object_or_404(Group, pk=pk)
    data = {
        'id': group.id,
        'name': group.name,
        'permissions': [permission.name for permission in group.permissions.all()]
    }
    return JsonResponse(data)

def permission_list_view(request):
    permissions = Permission.objects.all()
    data = [{'id': permission.id, 'name': permission.name} for permission in permissions]
    return JsonResponse(data)

def permission_detail_view(request, pk):
    permission = get_object_or_404(Permission, pk=pk)
    data = {'id': permission.id, 'name': permission.name}
    return JsonResponse(data)

def get_role_permissions(request, role_id):
    group = get_object_or_404(Group, id=role_id)
    permissions = group.permissions.all()
    permission_list = [permission.name for permission in permissions]
    return JsonResponse({'permissions': permission_list})

def assign_permission_to_role(request, role_id, permission_id):
    if not request.user.is_superuser:
        return JsonResponse({'error': 'Only superuser can assign permissions to roles'}, status=403)
    
    group = get_object_or_404(Group, id=role_id)
    permission = get_object_or_404(Permission, id=permission_id)
    group.permissions.add(permission)
    return JsonResponse({'message': 'Permission assigned successfully'})

# @permission_required(CAN_ASSIGN_TO_GROUP, raise_exception=True)
def assign_user_to_role(request, user_id, group_id):
    if request.method == 'POST':
        user = get_object_or_404(User, id=user_id)
        group = get_object_or_404(Group, id=group_id)

        # Assign the user to the group
        user.groups.add(group)
        return JsonResponse({'message': 'User assigned to group successfully'})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
    
def get_user_roles(request, user_id):
    user = User.objects.filter(id=user_id).first()
    if not user:
        return JsonResponse({'error': 'User not found'}, status=404)
    
    user_groups = user.groups.all()
    group_data = [{'id': group.id, 'name': group.name} for group in user_groups]
    
    return JsonResponse({'user_groups': group_data})