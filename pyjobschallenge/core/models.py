from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


class Student(models.Model):
    GRADE_CHOICES = [
        ("N1 - Educação Infantil", "N1 - Educação Infantil"),
        ("N2 - Educação Infantil", "N2 - Educação Infantil"),
        ("N3 - Educação Infantil", "N3 - Educação Infantil"),
        ("1º Ano - Ensino Fundamental", "1º Ano - Ensino Fundamental"),
        ("2º Ano - Ensino Fundamental", "2º Ano - Ensino Fundamental"),
        ("3º Ano - Ensino Fundamental", "3º Ano - Ensino Fundamental"),
        ("4º Ano - Ensino Fundamental", "4º Ano - Ensino Fundamental"),
        ("5º Ano - Ensino Fundamental", "5º Ano - Ensino Fundamental"),
        ("6º Ano - Ensino Fundamental", "6º Ano - Ensino Fundamental"),
        ("7º Ano - Ensino Fundamental", "7º Ano - Ensino Fundamental"),
        ("8º Ano - Ensino Fundamental", "8º Ano - Ensino Fundamental"),
        ("9º Ano - Ensino Fundamental", "9º Ano - Ensino Fundamental"),
        ("1º Ano - Ensino Médio", "1º Ano - Ensino Médio"),
        ("2º Ano - Ensino Médio", "2º Ano - Ensino Médio"),
        ("3º Ano - Ensino Médio", "3º Ano - Ensino Médio"),
    ]

    first_name = models.CharField(max_length=15, verbose_name="Nome")
    sur_name = models.CharField(max_length=40, verbose_name="Sobrenome")
    mothers_name = models.CharField(max_length=50, verbose_name="Nome da mãe")
    fathers_name = models.CharField(max_length=50, verbose_name="Nome do pai")
    date_of_birth = models.DateField(verbose_name="Data de nascimento")
    grade = models.CharField(
        max_length=50,
        verbose_name="Série",
        choices=GRADE_CHOICES
    )

    def __str__(self):
        return f"{self.first_name} {self.sur_name} - {self.grade}"


class SchoolSubject(models.Model):
    school_subject = models.CharField(
        max_length=30,
        verbose_name="Disciplina escolar",
        help_text="Model para armazenar as disciplinas escolares no banco de dados"
    )

    def __str__(self):
        return self.school_subject


class StudentSchoolSubject(models.Model):
    SCHOOL_PERIOD_CHOICES = [
        ("1º bimestre", "1º bimestre"),
        ("2º bimestre", "2º bimestre"),
        ("3º bimestre", "3º bimestre"),
        ("4º bimestre", "4º bimestre"),
    ]
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, verbose_name="Estudante"
    )
    subject = models.ForeignKey(
        SchoolSubject,
        on_delete=models.DO_NOTHING,
        verbose_name="Disciplina escolar",
        help_text="Disciplina escolar relacionada ao estudante"
    )
    subject_grade = models.FloatField(
        verbose_name="Nota", validators=[
            MaxValueValidator(limit_value=10),
            MinValueValidator(limit_value=0),
        ]
    )
    school_period = models.CharField(
        max_length=20,
        verbose_name="Período do ano",
        choices=SCHOOL_PERIOD_CHOICES,
    )

    def __str__(self):
        return f"{self.student} - {self.subject} - {self.subject_grade} - {self.school_period}"


class StudentApproved(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, verbose_name="Estudante"
    )
    approval = models.BooleanField(
        verbose_name="Estudante aprovado",
        help_text="Se o estudante passar de ano, o valor será True, se não, False"
    )
    year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1980),
            MaxValueValidator(timezone.now().year)
        ], verbose_name="Ano"
    )

    def __str__(self):
        if self.approval:
            return f"{self.student} - Aprovado - {self.year}"
        else:
            return f"{self.student} - Reprovado - {self.year}"
