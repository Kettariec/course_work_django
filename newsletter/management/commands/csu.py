from django.core.management import BaseCommand
from users.models import User
import os
from dotenv import load_dotenv
from config.settings import BASE_DIR

load_dotenv(BASE_DIR / '.env')


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email=os.getenv('SUPER_USER'),
            first_name='Admin',
            last_name='Adminov',
            is_superuser=True,
            is_staff=True,
            is_active=True
        )

        user.set_password(os.getenv('SUPER_USER_PASS'))
        user.save()
