# Generated by Django 3.0.8 on 2020-08-02 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentschoolsubject',
            name='school_period',
            field=models.CharField(choices=[('1º bimestre', '1º bimestre'), ('2º bimestre', '2º bimestre'), ('3º bimestre', '3º bimestre'), ('4º bimestre', '4º bimestre')], max_length=20, verbose_name='Período do ano'),
        ),
    ]
