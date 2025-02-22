from django.shortcuts import render
from students.models import Students
from django.http import JsonResponse

# Create your views here.

def StudentView(request):
    students = Students.objects.all()

    return JsonResponse(students, safe=False)