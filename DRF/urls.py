from django.urls import path
from DRFApi.views import StudentCRUDAPI
from django.contrib import admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path("student-crud/", StudentCRUDAPI.as_view(), name="student-list-create"),
    path("student-crud/<int:pk>/", StudentCRUDAPI.as_view(), name="student-detail"),    
]