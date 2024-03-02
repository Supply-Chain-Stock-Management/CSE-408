from django.contrib import admin
from .models import Profile, Activity

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'location', 'birth_date', 'email_subscribed']
    search_fields = ['user__username', 'first_name', 'last_name', 'location']
    list_filter = ['email_subscribed']

class ActivityAdmin(admin.ModelAdmin):
    list_display = ['user', 'activity_type', 'timestamp']
    search_fields = ['user__username', 'activity_type']
    list_filter = ['activity_type', 'timestamp']

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Activity, ActivityAdmin)
