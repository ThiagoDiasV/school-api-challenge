import pytest


@pytest.mark.usefixtures('student')
@pytest.mark.django_db
def test_student_str_method(student):
    assert str(student) == f"{student.first_name} {student.sur_name} - {student.grade}"


@pytest.mark.usefixtures('school_subject')
@pytest.mark.django_db
def test_school_subject_str_method(school_subject):
    assert str(school_subject) == school_subject.school_subject


@pytest.mark.usefixtures('student_school_subject')
@pytest.mark.django_db
def test_student_school_subject(student_school_subject):
    assert str(student_school_subject) == f"{student_school_subject.student} - {student_school_subject.subject} - {student_school_subject.subject_grade} - {student_school_subject.school_period}"


@pytest.mark.usefixtures('student_approved')
@pytest.mark.django_db
def test_student_approved_str_method(student_approved):
    assert str(student_approved) == f"{student_approved.student} - Aprovado - {student_approved.year}"


@pytest.mark.usefixtures('student_not_approved')
@pytest.mark.django_db
def test_student_not_approved_str_method(student_not_approved):
    assert str(student_not_approved) == f"{student_not_approved.student} - Reprovado - {student_not_approved.year}"
