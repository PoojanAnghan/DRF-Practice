from django.shortcuts import render
from DRFApi.serializers import StudentSerializer
from DRFApi.models import Student
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
import json
import io

# Create your views here.
def student_details(request, pk): 
    Stu = Student.objects.get(id=pk)
    # print(Stu)

    serialized = StudentSerializer(Stu)
    # print(serialized)
    
    # json_data = JSONRenderer().render(serialized.data)
    # print(json_data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serialized.data, safe=True)

def student_list(request): 
    if request.method == "GET":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id',None)
        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type = 'application/json')
        else:
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type = 'application/json')
    else:
        print("Post request")

@csrf_exempt
def student_opr(request):
    # ---------------- CREATE ----------------
    if request.method == "POST":
        stream = io.BytesIO(request.body)
        dict_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=dict_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'msg': 'Data created'}, status=201)
        return JsonResponse(serializer.errors, status=400)

    # ---------------- UPDATE ----------------
    elif request.method == "PUT":
        stream = io.BytesIO(request.body)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')

        try:
            stu = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return JsonResponse({"msg": "Student not found"}, status=404)

        serializer = StudentSerializer(stu, data=python_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"msg": "Updated Data"}, status=200)
        return JsonResponse(serializer.errors, status=400)

    # ---------------- DELETE ----------------
    elif request.method == "DELETE":
        stream = io.BytesIO(request.body)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')

        try:
            stu = Student.objects.get(id=id)
            stu.delete()
            return JsonResponse({"msg": "Student deleted"}, status=200)
        except Student.DoesNotExist:
            return JsonResponse({"msg": "Student not found"}, status=404)

    # ---------------- METHOD NOT ALLOWED ----------------
    return JsonResponse({"msg": "Method not allowed"}, status=405)