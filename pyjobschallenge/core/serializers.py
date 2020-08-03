from .models import Student, StudentApproved, StudentSchoolSubject, SchoolSubject
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class StudentApprovedSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentApproved
        fields = "__all__"


class StudentSchoolSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentSchoolSubject
        fields = "__all__"


class SchoolSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolSubject
        fields = "__all__"
