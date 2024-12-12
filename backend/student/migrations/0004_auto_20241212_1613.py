'''
Migrations to replace dummy data from `student_teacher` table with data from CSV file
'''

import csv
from django.db import migrations
from datetime import datetime


def load_teachers_from_csv(apps, schema_editor):
    Teacher = apps.get_model('student', 'Teacher')

    # Path to CSV file
    csv_file_path = 'student/data/teachers.csv'

    # Clear existing data
    Teacher.objects.all().delete()

    # Open and read csv file
    with open(csv_file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        teachers = []
        for row in reader:
            teachers.append(Teacher(
                first_name=row['first_name'],
                last_name=row['last_name'],
                email=row['email'],
                gender=row['gender'],
                hire_data=datetime.strptime(row['hire_date'], '%Y-%m-%d'),
                phone_number=row.get('phone_number', ''),
                address=row.get('address', ''),
                is_active=row['is_active'].lower() == 'true',
                created_at=datetime.now(),
                updated_at=datetime.now(),

            ))

        # Bulk insert
        Teacher.objects.bulk_create(teachers)

class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_teacher_course_teacher'),
    ]

    operations = [
        migrations.RunPython(load_teachers_from_csv),
    ]
