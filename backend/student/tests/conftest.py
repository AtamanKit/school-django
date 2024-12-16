import pytest
from student.models import Student


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
