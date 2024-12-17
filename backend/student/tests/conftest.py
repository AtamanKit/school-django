import pytest
from student.models import Student, Course, Teacher


# Check if the student is created successfully
@pytest.fixture
def student():
    return Student.objects.create(
        first_name='John',
        last_name='Doe',
        email='john.doe@example.com',
        date_of_birth = '1990-01-01',
        gender='M',
        enrollment_number='2020-001',
        date_of_enrollment='2020-01-01',
        program='B.Tech',
        is_active=True,
        created_at='2020-01-01T00:00:00Z',
        updated_at='2020-01-01T00:00:00Z',
    )

# Check if the teacher is created successfully
@pytest.fixture
def teacher():
    return Teacher.objects.create(
        first_name="Michael",
        last_name="Palin",
        email="michael.palin@example.com",
        hire_data="2020-01-01",
    )


# Check if the course is created successfully
@pytest.fixture
def course(teacher):
    return Course.objects.create(
        name='Python 101',
        code='PY101',
        description='Python Programming 101',
        credits=4,
        is_active=True,
        created_at='2020-01-01T00:00:00Z',
        teacher=teacher,
    )
