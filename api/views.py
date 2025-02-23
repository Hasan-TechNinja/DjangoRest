from django.shortcuts import render
from students.models import Student
from teacher.models import Teacher
from . serializers import StudentSerializer, TeacherSerializer

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.


@api_view(['GET', 'POST',])
def StudentView(request):
    if request.method == 'GET':
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors)
        

    elif request.method == 'PUT':
        student = Student.objects.get(pk = pk)
        serializer = StudentSerializer(student ,data = request.data,)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['PUT', 'GET'])
def StudentDetails(request, pk):
    try:
        student = Student.objects.get(pk = pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        student = Student.objects.get(pk = pk)
        serializer = StudentSerializer(student, many = False)
        return Response(serializer.data)

    elif request.method == 'PUT':    
        serializer = StudentSerializer(student, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeacherView(APIView):
    def get(self, request):
        teacher = Teacher.objects.all()
        serializer = TeacherSerializer(teacher, many = True)
        return Response(serializer.data, status=status.HTTP_302_FOUND)

    def post(self, request):
        serializer = TeacherSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)