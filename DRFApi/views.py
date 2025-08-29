from django.shortcuts import get_object_or_404
from DRFApi.serializers import StudentSerializer
from DRFApi.models import Student
from rest_framework.views import APIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import (
    ListModelMixin,         # list()
    CreateModelMixin,       # retrieve()
    RetrieveModelMixin,     # create()
    UpdateModelMixin,       # update() and partial_update()
    DestroyModelMixin       # destroy()
)
from rest_framework.generics import GenericAPIView
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
from DRFApi.CustomPermission import CusPermissions
from .CustomAuthentication import CustomAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
# -------------------- Simple Class APIview --------------------

class StudentCRUDAPI(APIView):

    def get(self, request, pk=None, format=None):
        if pk is not None:
            try:
                student = Student.objects.get(id=pk)
                serializer = StudentSerializer(student)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Student.DoesNotExist:
                return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            students = Student.objects.all()
            serializer = StudentSerializer(students, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        try:
            student = Student.objects.get(id=pk)
        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = StudentSerializer(student, data=request.data, partial=False)  # Full update
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Updated Data"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        try:
            student = Student.objects.get(id=pk)
        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = StudentSerializer(student, data=request.data, partial=True)  # Partial update
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Partially updated data"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            student = Student.objects.get(id=pk)
            student.delete()
            return Response({"msg": "Student deleted"}, status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)


# -------------------- GenericAPIView with Mixins --------------------

# Not required primary key
class LCStudentAPI(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)  # ListModelMixin

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)  # CreateModelMixin

# primary key required
class RUDStudentAPI(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        if "pk" in kwargs:  # /student-crud/<pk>/
            return self.retrieve(request, *args, **kwargs)
        return Response({"error": "Method not allowed"}, status=405)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# -------------------- Concreate View Classes --------------------
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

# -------------- ViewSet (Simple) ------------------ # don't combines the logic for multiple related

class StudentViewSet(viewsets.ViewSet):
    
    def list(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        try:
            student = Student.objects.get(pk=pk)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        try:
            student = Student.objects.get(pk=pk)
            student.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

# -------------------- GenericViewSet + Mixins -------------------- 
        

class StudentGenericViewSet(
    ListModelMixin,       
    RetrieveModelMixin,   
    CreateModelMixin,     
    UpdateModelMixin,      
    DestroyModelMixin,    
    viewsets.GenericViewSet
):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # Optional: override get_object to handle not found error
    def get_object(self):
        try:
            return super().get_object()
        except Student.DoesNotExist:
            from rest_framework.exceptions import NotFound
            raise NotFound("Student not found")
        
# -------------------- ModelViewSet - With modified method --------------------  # combines GenericViewSet + Mixins
        
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # Optional: custom create
    def create(self, request, *args, **kwargs):
        print("Creating a new student...")
        response = super().create(request, *args, **kwargs)
        response.data['message'] = "Student created successfully"
        return response

# -------------------- ReadOnlyModelViewSet -------------------- # Separate Viewset for only Read and Retrive data

class StudentReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer    


# ------------------------------------------------------------ Authenication ------------------------------------------------------------ 

class Authentication_test(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
# -------------------- Basic Authenication -------------------- 
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated] 
    # permission_classes = [IsAdminUser]    
    # permission_classes = [IsAuthenticatedOrReadOnly]  
    # permission_classes = [DjangoModelPermissions] 
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly] 
    

# -------------------- Session Authenication -------------------- 
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated] # Any Authenticated user acn access
    # permission_classes = [IsAdminUser]    # Only Admin user can 
    # permission_classes = [IsAuthenticatedOrReadOnly] # Is authentication failed then only safe opeartion can be performed 
    # permission_classes = [DjangoModelPermissions] # Give the accesses as defined in the user model in DB
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly] # Check the permission for each instance and unauthorized user will have only GET access


# -------------------- Custom Permissions --------------------
    # authentication_classes = [SessionAuthentication]
    # permission_classes=[CusPermissions]

# -------------------- TokenAuthentication --------------------
    # authentication_classes = [TokenAuthentication]
    # permission_classes=[IsAuthenticatedOrReadOnly]

# -------------------- Custom Autthentication --------------------
    # authentication_classes = [CustomAuthentication]  
    # permission_classes = [IsAuthenticated]

# -------------------- JWT Autthentication --------------------

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated] 