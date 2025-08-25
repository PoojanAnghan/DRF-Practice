# urls.py
from django.urls import path
from DRFApi.views import LCStudentAPI, RUDStudentAPI
from django.contrib import admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path("student-crud/", LCStudentAPI.as_view(), name="student-list-create"),
    path("student-crud/<int:pk>/", RUDStudentAPI.as_view(), name="student-detail"),
]
