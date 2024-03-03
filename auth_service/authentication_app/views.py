from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .forms import RegistrationForm
from django.contrib.auth.views import PasswordResetDoneView, PasswordResetCompleteView
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth import get_user_model
from .models import PendingUser
from django.contrib.auth.decorators import login_required, permission_required

from django.shortcuts import redirect
from django.contrib.auth.forms import SetPasswordForm
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Group
from django.conf import settings
from django.shortcuts import render
from .models import Entity
from django.utils.html import strip_tags
from profile_app.models import Profile
from django.http import HttpResponseNotFound



from permission_app.permission import (
    CAN_ASSIGN_PERMISSION,
    CAN_VIEW_PRODUCT,
    CAN_DELETE_USER,
    CAN_CONFIRM_SUPPLY,
    CAN_PURCHASE,
    CAN_CREATE_PRODUCT,
    CAN_VIEW_SHIPMENT,
    CAN_TRACK_TRANSPORT,
    CAN_MODIFY_PRODUCT,
    CAN_MANAGE_ORDERS,
    CAN_VIEW_PENDING_REQUESTS,
    CAN_REMOVE_USER,
    CAN_ASSIGN_TO_GROUP
)


def is_central_authority(user):
    central_authority_group = Group.objects.get(name='central_authority')
    return central_authority_group in user.groups.all()


currentUser = get_user_model()



@csrf_exempt
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            entity_id = request.POST.get('entity_id')  # Extract entity_id from form data
            entity = Entity.objects.get(pk=entity_id)  # Get the Entity object corresponding to the entity_id
            PendingUser.objects.create(email=email, username=username, entity=entity)  # Save PendingUser with associated entity
            return redirect('register_request_confirmation')
        else:
            # Concatenate form errors into a single message
            error_message = ', '.join([f"{field}: {', '.join(errors)}" for field, errors in form.errors.items()])
            # Render error.html template with the error message
            return render(request, 'error.html', {'message': error_message})
    else:
        entities = Entity.objects.all()  # Retrieve all entities from the database
        entity_map = {}  # Create a dictionary to store entities by type
        for entity in entities:
            if entity.type not in entity_map:
                entity_map[entity.type] = []
            entity_map[entity.type].append(entity)

        return render(request, 'register.html', {'entity_map': entity_map})



def request_confirm(request):
    return render(request, 'register_request_confirmation.html')




@login_required
@permission_required(CAN_VIEW_PENDING_REQUESTS, raise_exception=True)
def view_pending_requests(request):
    pending_users = PendingUser.objects.all()
    # Serialize pending_users as needed and return the data in JSON format
    return render(request, 'pending_requests.html', {'pending_users': pending_users})

@login_required
@permission_required(CAN_VIEW_PENDING_REQUESTS, raise_exception=True)
def approve_registration(request, pending_user_id):
    pending_user = PendingUser.objects.get(id=pending_user_id)
    
    # Create user from pending_user details
    user = User.objects.create_user(username=pending_user.username, email=pending_user.email)
    
    # Generate token for account activation
    token = default_token_generator.make_token(user)
    # uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
    uidb64 = user.pk
    # print(uidb64)
    # Build activation URL
    domain = get_current_site(request).domain
    activation_url = reverse('activate_account', kwargs={'uidb64': uidb64, 'token': token})
    activation_link = f'http://{domain}{activation_url}'

    print(uidb64)
    print(token)
    
    # Send activation email
    subject = 'Activate Your Account'
    html_message = render_to_string('activation_email.html', {'activation_link': activation_link})
    plain_message = strip_tags(html_message)  # Strip HTML tags for plain text message
    send_mail(subject, plain_message, None, [user.email], html_message=html_message)
    
    entity = pending_user.entity
    profile = Profile.objects.create(user=user, entity=entity)
    # Delete pending_user after approval
    pending_user.delete()
    
    return JsonResponse({'message': 'User registration approved. Activation email has been sent.'})


@login_required
@permission_required(CAN_VIEW_PENDING_REQUESTS, raise_exception=True)
def reject_registration(request, pending_user_id):
    pending_user = PendingUser.objects.get(id=pending_user_id)
    
    # Get entity details
    entity_name = pending_user.entity.name
    entity_location = pending_user.entity.location
    
    # Prepare email content
    subject = 'Registration Request Rejected'
    context = {
        'username': pending_user.username,
        'email': pending_user.email,
        'entity_name': entity_name,
        'entity_location': entity_location
    }
    email_html_message = render_to_string('reject_email_template.html', context)
    email_plain_message = strip_tags(email_html_message)  # Strip HTML tags for plain text message
    
    # Send rejection email
    send_mail(subject, email_plain_message, None, [pending_user.email], html_message=email_html_message)
    
    # Delete pending_user
    pending_user.delete()
    
    return JsonResponse({'message': 'User registration rejected. Rejection email has been sent.'})


def activate_account(request, uidb64, token):
    try:
        # uid = str(urlsafe_base64_decode(uidb64))
        uid = uidb64
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    

    print(user, token)
    if user is not None and default_token_generator.check_token(user, token):
        # Redirect to password set page
        return redirect('set_password', uidb64=uidb64, token=token)
    else:
        return JsonResponse({'error': 'Invalid activation link.'}, status=400)
    


def set_password(request, uidb64, token):
    """
    View for setting user's password after account activation.
    """
    # Decode the user ID and token
    # uid = str(urlsafe_base64_decode(uidb64))
    uid = uidb64
    try:
        user = User.objects.get(pk=uid)
    except User.DoesNotExist:
        return HttpResponseNotFound('<h1>User not found</h1>')

    # Check if the token is valid
    if default_token_generator.check_token(user, token):
        # Process password change
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'password_set_success.html')
            else:
                return JsonResponse({'errors': form.errors}, status=400)
        else:
            form = SetPasswordForm(user)
            return render(request, 'set_password.html', {'form': form})
    else:
        return HttpResponseNotFound('<h1>Invalid activation link</h1>')


@csrf_exempt
@permission_required(CAN_REMOVE_USER, raise_exception=True)
def remove_user(request, username):
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)

    user_to_remove = get_object_or_404(User, username=username)

    # Ensure the user making the request has the permission to remove users
    # and belongs to the central authority group
    if (is_central_authority(request.user) or request.user.is_superuser) and not user_to_remove.is_superuser:
        # Now you can safely delete the user
        user_to_remove.delete()
        return JsonResponse({'message': 'User removed successfully'})
    else:
        return JsonResponse({'error': 'You do not have permission to remove this user'}, status=403)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({'message': 'Login successful'})
            else:
                return JsonResponse({'error': 'Invalid username or password.'}, status=401)
        else:
            return JsonResponse({'error': 'Invalid form data.'}, status=400)
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return JsonResponse({'message': 'Logout successful'})


@login_required
def password_reset_view(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            # Get the user associated with the provided email
            user = request.user
            given_email = form.cleaned_data.get('email')
            if user is not None:
                # Generate token for password reset
                token = default_token_generator.make_token(user)
                uidb64 = user.pk
                
                # Build reset URL
                domain = get_current_site(request).domain
                reset_url = reverse('password_reset_confirm', kwargs={'uidb64': uidb64, 'token': token})
                reset_link = f'http://{domain}{reset_url}'

                # Render password reset email template
                subject = 'Password Reset Request'
                html_message = render_to_string('password_reset_email.html', {
                    'user': user,
                    'reset_link': reset_link,
                })
                plain_message = strip_tags(html_message)
                
                # Send email
                send_mail(subject, plain_message, None, [given_email], html_message=html_message)

            # Display success message
            message = 'Password reset email has been sent. Please check your email.'
            return render(request, 'password_reset_success.html', {'message': message})
        else:
            error_message = 'Invalid form data. Please check your inputs.'
            return render(request, 'password_reset.html', {'form': form, 'error_message': error_message})
    else:
        form = PasswordResetForm()
        return render(request, 'password_reset.html', {'form': form})


def password_reset_confirm_view(request, uidb64, token):
    try:
        # Decode the user ID from the base64 encoded string
        uid = uidb64
        # Get the user object
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    # Check if the user object exists and the token is valid
    if user is not None and default_token_generator.check_token(user, token):
        # Process password change
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'password_reset_success.html')
        else:
            form = SetPasswordForm(user)
        return render(request, 'password_reset_confirm.html', {'form': form})
    else:
        return render(request, 'password_reset_invalid.html')


# after a user submits a request to reset their password
class CustomPasswordResetDoneView(PasswordResetDoneView):
    def get(self, request, *args, **kwargs):
        return JsonResponse({'message': 'Password reset email has been sent. Please check your email.'})

# after the user has successfully reset their password
class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    def get(self, request, *args, **kwargs):
        return JsonResponse({'message': 'Password has been successfully reset.'})


# to save the user's changes after the password has been successfully changed
class CustomPasswordChangeView(PasswordChangeView):
    def form_valid(self, form):
        self.request.user.save()
        return JsonResponse({'message': 'Password changed successfully.'})

# for displaying a success message
class CustomPasswordChangeDoneView(PasswordChangeDoneView):
    def get(self, request, *args, **kwargs):
        return JsonResponse({'message': 'Password change done.'})
    



from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_info(request):
    # Retrieve user information
    user = request.user
    user_info = {
        'user_id': user.id,
        'entity_id': None,
        'username': user.username,
        'is_authenticated': user.is_authenticated,
    }

    # Check if the user has a profile
    try:
        profile = user.profile
        user_info['entity_id'] = profile.entity.id if profile.entity else None
    except Profile.DoesNotExist:
        pass

    # Return user information as JSON response
    return Response(user_info)