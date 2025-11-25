from django.core.management.base import BaseCommand
from chai.models import Student

class Command(BaseCommand):
    help = 'Populate the database with sample students'

    def handle(self, *args, **options):
        # Sample student data
        students_data = [
            {'name': 'Alice Johnson', 'age': 20, 'email': 'alice.johnson@example.com'},
            {'name': 'Bob Smith', 'age': 22, 'email': 'bob.smith@example.com'},
            {'name': 'Carol Davis', 'age': 19, 'email': 'carol.davis@example.com'},
            {'name': 'David Wilson', 'age': 21, 'email': 'david.wilson@example.com'},
            {'name': 'Eva Brown', 'age': 23, 'email': 'eva.brown@example.com'},
        ]

        # Clear existing students
        Student.objects.all().delete()
        self.stdout.write('Cleared existing students.')

        # Create new students
        for student_data in students_data:
            student = Student.objects.create(**student_data)
            self.stdout.write(f'Created student: {student}')

        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {len(students_data)} students!')
        )
