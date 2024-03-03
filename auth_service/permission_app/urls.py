from django.urls import path
from . import views

urlpatterns = [
    path('roles/', views.role_list_view, name='role_list'),
    path('roles/<int:pk>/', views.role_detail_view, name='role_detail'),
    path('permissions/', views.permission_list_view, name='permission_list'),
    path('permissions/<int:pk>/', views.permission_detail_view, name='permission_detail'),
    path('roles/<int:role_id>/permissions/', views.get_role_permissions, name='role_permissions'),
    path('roles/<int:role_id>/permissions/<int:permission_id>/assign/', views.assign_permission_to_role, name='assign_permission_to_role'),
    path('users/<int:user_id>/roles/', views.get_user_roles, name='user_roles'),
    path('users/<int:user_id>/roles/<int:group_id>/assign/', views.assign_user_to_role, name='assign_user_to_role'),
]
