from django.urls import path
from . import views

urlpatterns = [
    path('send/', views.send_email, name='send_email'),  # Endpoint to send emails
    path('email/logs/', views.email_logs_view, name='email_logs'),
    path('email/logs/<int:log_id>/', views.email_log_detail_view, name='email_log_detail'),
    path('subscribe/', views.subscribe_to_emails, name='subscribe_to_email'),
    path('unsubscribe/', views.unsubscribe_from_emails, name='unsubscribe_from_email'),
]
