from pyjobschallenge.core.models import (
    Student,
    StudentApproved,
    SchoolSubject,
    StudentSchoolSubject
)
import datetime
import pytest


@pytest.fixture
@pytest.mark.django_db
def student():
    first_name = "Estudante"
    sur_name = "De teste"
    mothers_name = "Mãe do estudante de teste"
    fathers_name = "Pai do estudante de teste"
    date_of_birth = datetime.date(2010, 6, 5)
    grade = "N1 - Educação Infantil"
    student = Student.objects.create(
        id=1,
        first_name=first_name,
        sur_name=sur_name,
        mothers_name=mothers_name,
        fathers_name=fathers_name,
        date_of_birth=date_of_birth,
        grade=grade
    )
    yield student
    student.delete()


@pytest.fixture
@pytest.mark.django_db
def school_subject():
    subject = "Matemática"
    school_subject = SchoolSubject.objects.create(
        id=1,
        school_subject=subject
    )
    yield school_subject
    school_subject.delete()


@pytest.fixture
@pytest.mark.django_db
def student_school_subject(student, school_subject):
    subject_grade = 8
    school_period = "1º bimestre"
    student_school_subject = StudentSchoolSubject.objects.create(
        id=1,
        student=student,
        subject=school_subject,
        subject_grade=subject_grade,
        school_period=school_period
    )
    yield student_school_subject
    student_school_subject.delete()


@pytest.fixture
@pytest.mark.django_db
def student_approved(student):
    approval = True
    year = 2020
    student_approved = StudentApproved.objects.create(
        id=1,
        student=student,
        approval=approval,
        year=year
    )
    yield student_approved
    student_approved.delete()


@pytest.fixture
@pytest.mark.django_db
def student_not_approved(student):
    approval = False
    year = 2020
    student_not_approved = StudentApproved.objects.create(
        id=2,
        student=student,
        approval=approval,
        year=year
    )
    yield student_not_approved
    student_not_approved.delete()
