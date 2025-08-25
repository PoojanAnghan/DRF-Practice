from django.contrib import admin
from django.urls import path
from DRFApi.views import student_details, student_list, student_opr
urlpatterns = [
    path("admin/", admin.site.urls),
    path("studentInfo/", student_list),
    path("studentInfo/<int:pk>", student_details),
    path("student/opr", student_opr)
]