from django.http import JsonResponse
from .models import EmailLog
from django.shortcuts import get_object_or_404
from profile_app.models import Profile
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def send_email(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        recipient_email = request.POST.get('recipient_email')
        
        if subject and message and recipient_email:
            try:
                send_mail(subject, message, None, [recipient_email])
                return JsonResponse({'message': 'Email sent successfully'})
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
        else:
            return JsonResponse({'error': 'Subject, message, and recipient email are required'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
    


def email_logs_view(request):
    """
    View to retrieve a list of email logs.
    """
    logs = EmailLog.objects.all()
    log_data = [{'id': log.id, 'recipient': log.recipient, 'timestamp': log.timestamp, 'status': log.status} for log in logs]
    return JsonResponse({'email_logs': log_data})

def email_log_detail_view(request, log_id):
    """
    View to retrieve details of a specific email log.
    """
    log = EmailLog.objects.filter(id=log_id).first()
    if not log:
        return JsonResponse({'error': 'Email log not found'}, status=404)
    
    log_data = {
        'id': log.id,
        'recipient': log.recipient,
        'timestamp': log.timestamp,
        'status': log.status,
        'subject': log.subject,
        'body': log.body,
        # Add more fields as needed
    }
    return JsonResponse(log_data)


def subscribe_to_emails(request, username):
    profile = get_object_or_404(Profile, user__username=username)
    profile.email_subscribed = True
    profile.save()
    return JsonResponse({'message': 'Successfully subscribed to email notifications'})

def unsubscribe_from_emails(request, username):
    profile = get_object_or_404(Profile, user__username=username)
    profile.email_subscribed = False
    profile.save()
    return JsonResponse({'message': 'Successfully unsubscribed from email notifications'})