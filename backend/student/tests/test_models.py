import pytest
from django.db import IntegrityError
from student.models import Student
from django.core.exceptions import ValidationError


# Check if the student is created successfully


@pytest.mark.django_db
def test_student_model(student):
    assert student.first_name == 'John'
    assert student.last_name == 'Doe'
    assert student.email == 'john.doe@example.com'


# Ensure that the __str__ method returns the full name
@pytest.mark.django_db
def test_student_str(student):
    assert str(student) == f"{student.first_name} {student.last_name}"


# Ensute the unique constraint on email field
@pytest.mark.django_db
def test_student_email_unique(student):
    with pytest.raises(IntegrityError):
        Student.objects.create(
            first_name='John',
            last_name='Doe',
            email=student.email,
            date_of_birth='1990-01-01',
            gender='M',
            enrollment_number='2020-002',
            date_of_enrollment='2020-01-01',
            program='B.Tech',
            is_active=True,
            created_at='2020-01-01T00:00:00Z',
            updated_at='2020-01-01T00:00:00Z',
        )

# Test validationo for fields, such as email, date_of_birth, or any custom validators
@pytest.mark.django_db
def test_student_invalid_email():
    student = Student(
        first_name='Invalid',
        last_name='Email',
        email = 'not-an-email',
        gender='O',
        enrollment_number='2020-003',
        date_of_birth='1990-01-01',
        date_of_enrollment='2020-01-01',
        program='B.Tech',
    )
    with pytest.raises(ValidationError):
        student.full_clean()

