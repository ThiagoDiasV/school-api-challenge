from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("estudantes", views.StudentViewSet, basename="students")
router.register("estudantes-aprovacao", views.StudentApprovedViewSet, basename="students_approval")
router.register("estudantes-materias", views.StudentSchoolSubjectViewSet, basename="students_school_subject")
router.register("materias-escolares", views.SchoolSubjectViewSet, basename="school_subject")

urlpatterns = [
    path("", include(router.urls)),
]
