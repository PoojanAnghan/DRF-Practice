# urls.py
from django.urls import path
# from DRFApi.views import LCStudentAPI, RUDStudentAPI
from DRFApi.views import StudentCreateAPI, StudentDeleteAPI, StudentListAPI, StudentRetrieveAPI, StudentUpdateAPI
from django.contrib import admin

# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path("student-crud/", LCStudentAPI.as_view(), name="student-list-create"),
#     path("student-crud/<int:pk>/", RUDStudentAPI.as_view(), name="student-detail"),
# ]

urlpatterns = [

    path('students/', StudentListAPI.as_view(), name='student-list'),
    path('students/create/', StudentCreateAPI.as_view(), name='student-create'),
    path('students/<int:pk>/', StudentRetrieveAPI.as_view(), name='student-retrieve'),
    path('students/<int:pk>/update/', StudentUpdateAPI.as_view(), name='student-update'),
    path('students/<int:pk>/delete/', StudentDeleteAPI.as_view(), name='student-delete'),
]