from django.apps import AppConfig

class BookingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Bookings'

    def ready(self):
        import Bookings.signals
        from django.db.models.signals import post_migrate
        from django.contrib.auth import get_user_model

        def create_default_superuser(sender, **kwargs):
            User = get_user_model()
            if not User.objects.filter(username='admin').exists():
                User.objects.create_superuser(
                    username='admin',
                    email='admin@example.com',
                    password='AdminPassword123'
                )

        post_migrate.connect(create_default_superuser, sender=self)
