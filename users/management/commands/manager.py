from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        # content_type_1 = ContentType.objects.get(app_label='newsletter', model='newsletter')
        # content_type_2 = ContentType.objects.get(app_label='users', model='user')
        # Permission.objects.create(codename='set_status', name='Can change status', content_type=content_type_1)
        # Permission.objects.create(codename='set_is_active', name='Can deactivate user', content_type=content_type_2)

        manager_group = Group.objects.create(name='manager')
        # manager_group = Group.objects.get(name='manager')

        perm_1 = Permission.objects.get(content_type__app_label='newsletter', content_type__model='newsletter',
                                        codename='view_newsletter')
        perm_2 = Permission.objects.get(content_type__app_label='users', content_type__model='user',
                                        codename='view_user')
        perm_3 = Permission.objects.get(content_type__app_label='users', content_type__model='user',
                                        codename='set_is_active')
        perm_4 = Permission.objects.get(content_type__app_label='newsletter', content_type__model='newsletter',
                                        codename='set_status')

        manager_group.permissions.add(perm_1)
        manager_group.permissions.add(perm_2)
        manager_group.permissions.add(perm_3)
        manager_group.permissions.add(perm_4)
