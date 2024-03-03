from django.contrib import admin
from .models import PendingUser, Entity

class PendingUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'created_at']
    search_fields = ['username', 'email']
    list_filter = ['created_at']

admin.site.register(PendingUser, PendingUserAdmin)


@admin.register(Entity)
class EntityAdmin(admin.ModelAdmin):
    list_display = ('entity_id', 'type', 'name', 'location')
    search_fields = ('entity_id', 'type', 'name', 'location')
    list_filter = ('type', 'location')
