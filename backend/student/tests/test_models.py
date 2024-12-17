import pytest
from django.db import IntegrityError
from student.models import Student, Course, Teacher
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

# Test validation for fields, such as email, date_of_birth, or any custom validators
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


# Test to delete a student
@pytest.mark.django_db
def test_delete_student(student):
    
    # Verify that the student is present
    assert Student.objects.filter(id=student.id).exists()

    # Delete the student
    student.delete()
    
    # Verify that the student is deleted
    assert not Student.objects.filter(id=student.id).exists()


# Check relationship between Student and Course
@pytest.mark.django_db
def test_student_course_relationship(student, course):
    # Add the course to the student
    student.courses.add(course)

    # Verify the relationship
    assert course in student.courses.all()
    assert student in course.students.all()

    # Verify count
    assert student.courses.count() == 1
    assert course.students.count() == 1


# Verify that the relationship can be removed
@pytest.mark.django_db
def test_remove_course_from_student(student, course):
    # Add the course to the student
    student.courses.add(course)

    # Remove the course
    student.courses.remove(course)

    # Verify the relationship no longer exists
    assert course not in student.courses.all()
    assert student not in course.students.all()

    # Verify count
    assert student.courses.count() == 0
    assert course.students.count() == 0


# Verify ForeignKey relationship between Course and Teacher
@pytest.mark.django_db
def test_course_teacher_relationship(course, teacher):
    # Verify the teacher is correctly assigned to the course
    assert course.teacher == teacher
    assert teacher.courses.count() == 1
    assert course in teacher.courses.all()


# Verify that when a Teacher is deleted, all their related Course instances are also deleted (due to on_delete=models.CASCADE).
@pytest.mark.django_db
def test_teacher_deletion_cascade(teacher, course):
    # Verify the course exists
    assert Course.objects.filter(id=course.id).exists()

    # Delete the teacher
    teacher.delete()

    # Verify the course is also deleted
    assert not Course.objects.filter(id=course.id).exists()
