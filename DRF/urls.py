from django.contrib import admin
from django.urls import path
from DRFApi.views import student_details, student_list, new_student

urlpatterns = [
    path("admin/", admin.site.urls),
    path("studentInfo/", student_list),
    path("studentInfo/<int:pk>", student_details),
    path("student/add", new_student),
]
