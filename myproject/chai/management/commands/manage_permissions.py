from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Permission, Group
from django.contrib.contenttypes.models import ContentType
from chai.models import Student

class Command(BaseCommand):
    help = 'Manage user permissions for the Student model'

    def add_arguments(self, parser):
        parser.add_argument('--action', choices=['list', 'create', 'assign', 'remove'], 
                          help='Action to perform')
        parser.add_argument('--username', help='Username to manage')
        parser.add_argument('--permission', help='Permission codename')
        parser.add_argument('--group', help='Group name')

    def handle(self, *args, **options):
        action = options['action']
        
        if action == 'list':
            self.list_permissions()
        elif action == 'create':
            self.create_groups()
        elif action == 'assign':
            self.assign_permissions(options['username'], options['permission'], options['group'])
        elif action == 'remove':
            self.remove_permissions(options['username'], options['permission'], options['group'])
        else:
            self.show_help()

    def list_permissions(self):
        """List all available permissions and current user permissions"""
        self.stdout.write(self.style.SUCCESS('=== AVAILABLE PERMISSIONS ==='))
        
        # Get Student model permissions
        content_type = ContentType.objects.get_for_model(Student)
        permissions = Permission.objects.filter(content_type=content_type)
        
        self.stdout.write('\nStudent Model Permissions:')
        for perm in permissions:
            self.stdout.write(f'- {perm.codename}: {perm.name}')
        
        # List all users and their permissions
        self.stdout.write('\n=== USER PERMISSIONS ===')
        users = User.objects.all()
        for user in users:
            self.stdout.write(f'\nUser: {user.username} (ID: {user.id})')
            self.stdout.write(f'  Is Superuser: {user.is_superuser}')
            self.stdout.write(f'  Is Staff: {user.is_staff}')
            self.stdout.write(f'  Is Active: {user.is_active}')
            
            # Direct permissions
            direct_perms = user.user_permissions.filter(content_type=content_type)
            if direct_perms:
                self.stdout.write('  Direct Permissions:')
                for perm in direct_perms:
                    self.stdout.write(f'    - {perm.codename}: {perm.name}')
            
            # Group permissions
            groups = user.groups.all()
            if groups:
                self.stdout.write('  Groups:')
                for group in groups:
                    self.stdout.write(f'    - {group.name}')
                    group_perms = group.permissions.filter(content_type=content_type)
                    for perm in group_perms:
                        self.stdout.write(f'      - {perm.codename}: {perm.name}')

    def create_groups(self):
        """Create useful permission groups"""
        self.stdout.write('Creating permission groups...')
        
        # Student Manager Group
        student_manager, created = Group.objects.get_or_create(name='Student Manager')
        if created:
            self.stdout.write('✅ Created "Student Manager" group')
        
        # Add permissions to Student Manager
        content_type = ContentType.objects.get_for_model(Student)
        permissions = Permission.objects.filter(content_type=content_type)
        student_manager.permissions.set(permissions)
        self.stdout.write('✅ Added all Student permissions to Student Manager group')
        
        # Student Viewer Group (read-only)
        student_viewer, created = Group.objects.get_or_create(name='Student Viewer')
        if created:
            self.stdout.write('✅ Created "Student Viewer" group')
        
        # Add only view permissions
        view_perms = permissions.filter(codename__in=['view_student'])
        student_viewer.permissions.set(view_perms)
        self.stdout.write('✅ Added view permissions to Student Viewer group')
        
        # Student Editor Group (add, change, view)
        student_editor, created = Group.objects.get_or_create(name='Student Editor')
        if created:
            self.stdout.write('✅ Created "Student Editor" group')
        
        # Add add, change, view permissions
        edit_perms = permissions.filter(codename__in=['add_student', 'change_student', 'view_student'])
        student_editor.permissions.set(edit_perms)
        self.stdout.write('✅ Added edit permissions to Student Editor group')

    def assign_permissions(self, username, permission, group):
        """Assign permissions to a user"""
        try:
            user = User.objects.get(username=username)
            
            if group:
                # Assign user to group
                group_obj = Group.objects.get(name=group)
                user.groups.add(group_obj)
                self.stdout.write(f'✅ Added {username} to group: {group}')
            
            if permission:
                # Assign specific permission
                content_type = ContentType.objects.get_for_model(Student)
                perm_obj = Permission.objects.get(codename=permission, content_type=content_type)
                user.user_permissions.add(perm_obj)
                self.stdout.write(f'✅ Added permission {permission} to user {username}')
                
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'User {username} not found'))
        except Group.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Group {group} not found'))
        except Permission.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Permission {permission} not found'))

    def remove_permissions(self, username, permission, group):
        """Remove permissions from a user"""
        try:
            user = User.objects.get(username=username)
            
            if group:
                # Remove user from group
                group_obj = Group.objects.get(name=group)
                user.groups.remove(group_obj)
                self.stdout.write(f'✅ Removed {username} from group: {group}')
            
            if permission:
                # Remove specific permission
                content_type = ContentType.objects.get_for_model(Student)
                perm_obj = Permission.objects.get(codename=permission, content_type=content_type)
                user.user_permissions.remove(perm_obj)
                self.stdout.write(f'✅ Removed permission {permission} from user {username}')
                
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'User {username} not found'))
        except Group.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Group {group} not found'))
        except Permission.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Permission {permission} not found'))

    def show_help(self):
        """Show usage examples"""
        self.stdout.write(self.style.SUCCESS('=== PERMISSION MANAGEMENT COMMANDS ==='))
        self.stdout.write('\n1. List all permissions and users:')
        self.stdout.write('   python manage.py manage_permissions --action list')
        
        self.stdout.write('\n2. Create permission groups:')
        self.stdout.write('   python manage.py manage_permissions --action create')
        
        self.stdout.write('\n3. Assign user to group:')
        self.stdout.write('   python manage.py manage_permissions --action assign --username Dependra --group "Student Manager"')
        
        self.stdout.write('\n4. Assign specific permission:')
        self.stdout.write('   python manage.py manage_permissions --action assign --username Dependra --permission add_student')
        
        self.stdout.write('\n5. Remove permission:')
        self.stdout.write('   python manage.py manage_permissions --action remove --username Dependra --permission delete_student')
        
        self.stdout.write('\n=== AVAILABLE PERMISSIONS ===')
        self.stdout.write('- add_student: Can add student')
        self.stdout.write('- change_student: Can change student')
        self.stdout.write('- delete_student: Can delete student')
        self.stdout.write('- view_student: Can view student')
