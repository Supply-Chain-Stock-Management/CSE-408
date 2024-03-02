from django.contrib import admin
from .models import EmailLog

class EmailLogAdmin(admin.ModelAdmin):
    list_display = ['recipient', 'timestamp', 'status', 'subject']
    search_fields = ['recipient', 'subject']
    list_filter = ['status', 'timestamp']

admin.site.register(EmailLog, EmailLogAdmin)
