from django.contrib import admin
from django.urls import path, include
from DRFApi.views import LCStudentAPI, RUDStudentAPI   # ---- GenericClassview + Mixins
from DRFApi.views import StudentCreateAPI, StudentListAPI, StudentRetrieveAPI, StudentUpdateAPI # StudentDeleteAPI  ---- Concreate View
from DRFApi.views import StudentViewSet, StudentGenericViewSet # ---- ViewSet
from DRFApi.views import Authentication_test # Class having an authentication
from rest_framework.routers import DefaultRouter

# -------------------  GenericClassview + Mixins -------------------
# urlpatterns = [ 
#         path("admin/", admin.site.urls),
#         path("student-crud/", LCStudentAPI.as_view(), name="student-list-create"),
#         path("student-crud/<int:pk>/", RUDStudentAPI.as_view(), name="student-detail"),
# ]


# ------------------- Concreate View -------------------
# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path('students/', StudentListAPI.as_view(), name='student-list'),
#     path('students/create/', StudentCreateAPI.as_view(), name='student-create'),
#     path('students/<int:pk>/', StudentRetrieveAPI.as_view(), name='student-retrieve'),
#     # path('students/<int:pk>/update/', StudentUpdateAPI.as_view(), name='student-update'),
#     # path('students/<int:pk>/delete/', StudentDeleteAPI.as_view(), name='student-delete'),
# ]

# ------------------- ViewSet(simple) -------------------

router = DefaultRouter()
# router.register(r'students', StudentViewSet, basename='student')
# router.register(r'students', StudentGenericViewSet, basename='student')
router.register(r'students', Authentication_test, basename='student')

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls)),
]