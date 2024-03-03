from django.urls import path
from . import views

urlpatterns = [
    path('profile/<str:username>/', views.profile_view, name='profile_view'),
    path('profile/<str:username>/update/', views.profile_update_view, name='profile_update_view'),
    path('activity/log/', views.activity_log_view, name='activity_log_view'),
]
