from pyjobschallenge.core.serializers import (
    StudentSerializer,
    StudentApprovedSerializer,
    StudentSchoolSubjectSerializer,
    SchoolSubjectSerializer
)
import pytest


@pytest.mark.usefixtures('student')
@pytest.mark.django_db
def test_student_serializer(student):
    serializer = StudentSerializer(student)
    student_first_name = serializer.data['first_name']
    student_sur_name = serializer.data['sur_name']
    student_grade = serializer.data['grade']
    assert 'Estudante' == student_first_name
    assert 'De teste' == student_sur_name
    assert 'N1 - Educação Infantil' == student_grade


@pytest.mark.usefixtures('school_subject')
@pytest.mark.django_db
def test_school_subject(school_subject):
    serializer = SchoolSubjectSerializer(school_subject)
    subject = serializer.data['school_subject']
    assert 'Matemática' == subject


@pytest.mark.usefixtures('student_school_subject')
@pytest.mark.django_db
def test_student_school_subject(student_school_subject):
    serializer = StudentSchoolSubjectSerializer(student_school_subject)
    subject_grade = serializer.data['subject_grade']
    assert 8 == subject_grade


@pytest.mark.usefixtures('student_approved')
@pytest.mark.django_db
def test_student_approved(student_approved):
    serializer = StudentApprovedSerializer(student_approved)
    approval = serializer.data['approval']
    assert approval is True
