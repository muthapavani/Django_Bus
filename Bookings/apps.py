from django.apps import AppConfig
from django.contrib.auth import get_user_model

class BookingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Bookings'

    def ready(self):
        # Import your signals as before
        import Bookings.signals

        # Create superuser if it doesn't exist
        User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='pavani',
                email='pavani@example.com',
                password='123456'
            )
