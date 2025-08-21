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
    Stu = Student.objects.all()
    # print(Stu)
    serialized = StudentSerializer(Stu, many=True)
    # print(serialized)
    # json_data = JSONRenderer().render(serialized.data)
    # print(json_data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serialized.data, safe=False)

@csrf_exempt
def new_student(request):
    if request.method == "POST":
        stream = io.BytesIO(request.body)
        dict_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=dict_data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'msg': 'Data created'}, status=201)

        return JsonResponse(serializer.errors, status=400)
        