from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    """
    custom command for creating superuser
    python3 manage.py csu
    command for using this command
    """
    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@sky.pro',
            first_name='Admin',
            last_name='SkyPro',
            is_staff=True,
            is_superuser=True
        )
        user.set_password('qwert')
        user.save()
