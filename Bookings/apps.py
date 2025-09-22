from django.apps import AppConfig
from django.contrib.auth import get_user_model
from django.db.utils import OperationalError

class BookingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Bookings'

    def ready(self):
        import Bookings.signals

        try:
            User = get_user_model()
            if not User.objects.filter(username='admin').exists():
                User.objects.create_superuser(
                    username='admin',
                    email='admin@example.com',
                    password='AdminPassword123'
                )
        except OperationalError:
            pass
        except Exception as e:
            print(f"Skipping superuser creation: {e}")
