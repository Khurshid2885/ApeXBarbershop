from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        # from accounts.signals import send_welcome_email
        from accounts.signals import auto_create_barber_profile
