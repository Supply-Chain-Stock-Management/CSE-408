from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Profile, Activity
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

@csrf_exempt
def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    profile_data = {
        'username': user.username,
        'email': user.email,
        'first_name': profile.first_name,
        'last_name': profile.last_name,
        'bio': profile.bio,
        'location': profile.location,
        'birth_date': profile.birth_date.strftime('%Y-%m-%d') if profile.birth_date else None,
        # Add other profile fields as needed
    }
    return JsonResponse(profile_data)

@csrf_exempt
def profile_update_view(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)

    if request.method == 'POST':
        # Update profile fields based on request data
        for field_name, field_value in request.POST.items():
            if hasattr(profile, field_name):
                setattr(profile, field_name, field_value)
        profile.save()
        return JsonResponse({'message': 'Profile updated successfully'})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)


@csrf_exempt
def activity_log_view(request):
    if request.method != 'GET':
        return JsonResponse({'error': 'Only GET requests are allowed.'}, status=405)

    # Retrieve and filter activity log entries for the current user
    activity_log = Activity.objects.filter(user=request.user).order_by('-timestamp')
    
    # Prepare activity log data as JSON
    activity_data = []
    for activity in activity_log:
        activity_data.append({
            'timestamp': activity.timestamp,
            'activity_type': activity.activity_type,
            # Add more fields if needed
        })

    return JsonResponse({'activity_log': activity_data})


