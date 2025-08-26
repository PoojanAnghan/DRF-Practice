from DRFApi.serializers import StudentSerializer
from DRFApi.models import Student
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
)
from rest_framework.generics import GenericAPIView
from rest_framework import generics


# -------------------- Simple Class APIview --------------------

# class StudentCRUDAPI(APIView):

#     def get(self, request, pk=None, format=None):
#         if pk is not None:
#             try:
#                 student = Student.objects.get(id=pk)
#                 serializer = StudentSerializer(student)
#                 return Response(serializer.data, status=status.HTTP_200_OK)
#             except Student.DoesNotExist:
#                 return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
#         else:
#             students = Student.objects.all()
#             serializer = StudentSerializer(students, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request, format=None):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"msg": "Data created"}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, pk, format=None):
#         try:
#             student = Student.objects.get(id=pk)
#         except Student.DoesNotExist:
#             return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

#         serializer = StudentSerializer(student, data=request.data, partial=False)  # Full update
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"msg": "Updated Data"}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def patch(self, request, pk, format=None):
#         try:
#             student = Student.objects.get(id=pk)
#         except Student.DoesNotExist:
#             return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

#         serializer = StudentSerializer(student, data=request.data, partial=True)  # Partial update
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"msg": "Partially updated data"}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         try:
#             student = Student.objects.get(id=pk)
#             student.delete()
#             return Response({"msg": "Student deleted"}, status=status.HTTP_200_OK)
#         except Student.DoesNotExist:
#             return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)


# -------------------- GenericAPIView with Mixins --------------------

# class LCStudentAPI(GenericAPIView, ListModelMixin, CreateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)  # ListModelMixin

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)  # CreateModelMixin

# class RUDStudentAPI(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def get(self, request, *args, **kwargs):
#         if "pk" in kwargs:  # /student-crud/<pk>/
#             return self.retrieve(request, *args, **kwargs)
#         return Response({"error": "Method not allowed"}, status=405)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def patch(self, request, *args, **kwargs):
#         return self.partial_update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

class StudentListAPI(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentCreateAPI(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveAPI(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentUpdateAPI(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDeleteAPI(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer