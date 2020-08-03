from .models import (
    Student,
    StudentApproved,
    SchoolSubject,
    StudentSchoolSubject
)
from .serializers import (
    StudentSerializer,
    StudentApprovedSerializer,
    SchoolSubjectSerializer,
    StudentSchoolSubjectSerializer,
)
from django_filters import rest_framework as filters
from rest_framework import viewsets


class FilterBackends:
    filter_backends = (filters.DjangoFilterBackend)
    filterset_fields = "__all__"


class StudentViewSet(viewsets.ModelViewSet, FilterBackends):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentApprovedViewSet(viewsets.ModelViewSet, FilterBackends):
    queryset = StudentApproved.objects.all()
    serializer_class = StudentApprovedSerializer


class StudentSchoolSubjectViewSet(viewsets.ModelViewSet, FilterBackends):
    queryset = StudentSchoolSubject.objects.all()
    serializer_class = StudentSchoolSubjectSerializer


class SchoolSubjectViewSet(viewsets.ModelViewSet, FilterBackends):
    queryset = SchoolSubject.objects.all()
    serializer_class = SchoolSubjectSerializer
