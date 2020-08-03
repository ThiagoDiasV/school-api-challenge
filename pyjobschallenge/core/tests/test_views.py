from django.forms.models import model_to_dict
import datetime
import pytest


@pytest.mark.django_db
@pytest.mark.parametrize('url', [
    '/estudantes/',
    '/estudantes-aprovacao/',
    '/estudantes-materias/',
    '/materias-escolares/',
]
)
def test_get_of_all_urls(client, url):
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_new_student(client):
    data = {
        'first_name': 'Estudante',
        'sur_name': 'Novo',
        'mothers_name': 'Mãe do novo estudante',
        'fathers_name': 'Pai do novo estudante',
        'date_of_birth': datetime.date(2016, 5, 5),
        'grade': "1º Ano - Ensino Fundamental"
    }
    response = client.post('/estudantes/', data)
    assert response.status_code == 201


@pytest.mark.usefixtures('student')
@pytest.mark.django_db
def test_update_existing_student(student, client):
    data = model_to_dict(student)
    data['grade'] = "N2 - Educação Infantil"
    response = client.put(
        '/estudantes/1/',
        data=data,
        content_type="application/json"
    )
    assert response.status_code == 200


@pytest.mark.parametrize(
    'url',
    [
        '/estudantes/1/',
        '/estudantes-aprovacao/1/',
        '/estudantes-materias/1/',
        '/materias-escolares/1/',
    ]
)
@pytest.mark.usefixtures(
    'student',
    'student_approved',
    'student_school_subject',
    'school_subject',
)
@pytest.mark.django_db
def test_destroy_existing_data(
    student,
    student_approved,
    student_school_subject,
    school_subject,
    client,
    url
):
    response = client.delete(
        url,
    )
    assert response.status_code == 204


@pytest.mark.django_db
def test_create_school_subject(client):
    data = {
        'school_subject': 'Biologia'
    }
    response = client.post(
        '/materias-escolares/',
        data
    )
    assert response.status_code == 201


@pytest.mark.usefixtures('school_subject')
@pytest.mark.django_db
def test_update_school_subject(school_subject, client):
    data = {
        'school_subject': "Geografia"
    }
    response = client.put(
        '/materias-escolares/1/',
        data,
        content_type="application/json",
    )
    assert response.status_code == 200


@pytest.mark.usefixtures('student', 'school_subject')
@pytest.mark.django_db
def test_create_student_school_subject(student, school_subject, client):
    data = {
        'student': student.id,
        'subject': school_subject.id,
        'subject_grade': 8,
        'school_period': "1º bimestre",
    }
    response = client.post(
        '/estudantes-materias/',
        data,
    )
    assert response.status_code == 201


@pytest.mark.usefixtures(
    'student_school_subject',
    'student',
    'school_subject',
)
@pytest.mark.django_db
def test_update_student_school_subject(
    student_school_subject,
    student,
    school_subject,
    client
):
    data = {
        'student': student.id,
        'subject': school_subject.id,
        'subject_grade': 7,
        'school_period': '2º bimestre'
    }
    response = client.put(
        '/estudantes-materias/1/',
        data,
        content_type="application/json"
    )
    assert response.status_code == 200


@pytest.mark.usefixtures('student')
@pytest.mark.django_db
def test_create_student_approved_data(student, client):
    data = {
        'student': student.id,
        'approval':True,
        'year': 2020
    }
    response = client.post(
        '/estudantes-aprovacao/',
        data,
    )
    assert response.status_code == 201


@pytest.mark.usefixtures('student_approved', 'student')
@pytest.mark.django_db
def test_update_student_approved(student_approved, student, client):
    data = {
        'student': student.id,
        'approval': False,
        'year': student_approved.year
    }
    response = client.put(
        '/estudantes-aprovacao/1/',
        data,
        content_type="application/json"
    )
    assert response.status_code == 200
