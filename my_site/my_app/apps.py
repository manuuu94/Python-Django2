from django.apps import AppConfig


class MyAppConfig(AppConfig): #include in settings to use templates,etc in app level.
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_app'
