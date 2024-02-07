from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        # content_type_1 = ContentType.objects.get(app_label='newsletter', model='newsletter')
        # content_type_2 = ContentType.objects.get(app_label='users', model='users')

        # Permission.objects.create(codename='set_status', name='Can change status', content_type=content_type_1)
        # Permission.objects.create(codename='set_is_active', name='Can deactivate user', content_type=content_type_2)

        perm_1 = Permission.objects.get(content_type__app_label='newsletter',
                                        content_type__model='newsletter', codename='can_view')
        perm_2 = Permission.objects.get(content_type__app_label='users',
                                        content_type__model='users', codename='can_view')
        perm_3 = Permission.objects.get(content_type__app_label='users',
                                        content_type__model='users', codename='can_deactivate')
        perm_4 = Permission.objects.get(content_type__app_label='newsletter',
                                        content_type__model='newsletter', codename='set_status')

        manager_group = Group.objects.get(name='manager')

        manager_group.permissions.add(perm_1)
        manager_group.permissions.add(perm_2)
        manager_group.permissions.add(perm_3)
        manager_group.permissions.add(perm_4)
