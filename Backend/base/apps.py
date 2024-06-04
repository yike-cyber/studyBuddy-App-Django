
# Backend/base/apps.py

from django.apps import AppConfig

class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Backend.base'
    def ready(self):
        from . import online_status
