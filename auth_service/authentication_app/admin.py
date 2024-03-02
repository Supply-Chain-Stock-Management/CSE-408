from django.contrib import admin
from .models import PendingUser

class PendingUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'created_at']
    search_fields = ['username', 'email']
    list_filter = ['created_at']

admin.site.register(PendingUser, PendingUserAdmin)
