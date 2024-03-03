from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('pending-requests/', views.view_pending_requests, name='view_pending_requests'),
    path('approve-registration/<int:pending_user_id>/', views.approve_registration, name='approve_registration'),
    path('reject-registration/<int:pending_user_id>/', views.reject_registration, name='reject_registration'),
    path('activate-account/<int:uidb64>/<str:token>/', views.activate_account, name='activate_account'),
    path('set-password/<int:uidb64>/<str:token>/', views.set_password, name='set_password'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('password-reset/', views.password_reset_view, name='password_reset'),
    path('password-reset-confirm/<int:uidb64>/<str:token>/', views.password_reset_confirm_view, name='password_reset_confirm'),
    path('password-reset-done/', views.CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-complete/', views.CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password-change/', views.CustomPasswordChangeView.as_view(), name='password_change'),
    path('password-change-done/', views.CustomPasswordChangeDoneView.as_view(), name='password_change_done'),
    path('remove-user/<str:username>/', views.remove_user, name='remove_user'),
    path('register/request_confirm/', views.request_confirm, name='register_request_confirmation'),
    path('user-info/', views.get_user_info, name='user_info'),

]
