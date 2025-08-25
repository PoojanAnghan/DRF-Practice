from django.shortcuts import get_object_or_404
from DRFApi.serializers import StudentSerializer
from DRFApi.models import Student
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# ---------------- Single Student (GET by ID) ----------------
class StudentDetailAPI(APIView):
    def get(self, request, pk, format=None):
        stu = get_object_or_404(Student, id=pk)
        serializer = StudentSerializer(stu)
        return Response(serializer.data, status=status.HTTP_200_OK)


# ---------------- All Students (GET List) ----------------
class StudentListAPI(APIView):
    def get(self, request, format=None):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# ---------------- CRUD Operations ----------------
class StudentCRUDAPI(APIView):
    # CREATE
    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # UPDATE (partial update allowed)
    def put(self, request, format=None):
        student_id = request.data.get('id')
        stu = get_object_or_404(Student, id=student_id)

        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Updated Data"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE
    def delete(self, request, format=None):
        student_id = request.data.get('id')
        stu = get_object_or_404(Student, id=student_id)
        stu.delete()
        return Response({"msg": "Student deleted"}, status=status.HTTP_200_OK)
