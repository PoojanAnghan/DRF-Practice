from django.urls import path
from DRFApi.views import StudentDetailAPI, StudentListAPI, StudentCRUDAPI

urlpatterns = [
    path("student/<int:pk>/", StudentDetailAPI.as_view(), name="student-detail"),
    path("students/", StudentListAPI.as_view(), name="student-list"),
    path("student-crud/", StudentCRUDAPI.as_view(), name="student-crud"),
]
