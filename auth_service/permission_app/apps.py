from django.apps import AppConfig
# from django.db.models.signals import post_migrate
# from .permission import create_custom_permissions

class PermissionAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'permission_app'

    # def ready(self):
    #     # Connect the create_custom_permissions function to the post_migrate signal
    #     post_migrate.connect(create_custom_permissions, sender=self)
