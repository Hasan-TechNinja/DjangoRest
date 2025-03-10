from django.shortcuts import render, get_object_or_404
from students.models import Student
from teacher.models import Teacher
from Employee.models import Employee

from . serializers import StudentSerializer, TeacherSerializer, EmployeeSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, mixins, generics, viewsets
from rest_framework.views import APIView

from blogs.models import Blog, Comment
from blogs.serializers import BlogSerializer, CommentSerializer


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
        
    def put(self, request, pk):
        teacher = Teacher.objects.get(id=pk)
        serializer = TeacherSerializer(teacher, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class TeacherDetails(APIView):
    def get(self, request, pk):
        try: 
            teacher = Teacher.objects.get(pk = pk)
        except Teacher.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TeacherSerializer(teacher, many=False)
        return Response(serializer.data)

    def put(self, request, pk):
        teacher = Teacher.objects.get(pk= pk)
        serializer = TeacherSerializer(teacher, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        teacher = Teacher.objects.get(pk=pk)
        teacher.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)
'''
#Mixin view with Create, Read, Update and Delete operation
class EmployeView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)
    

class EmployeDetailsView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,mixins.DestroyModelMixin , generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, pk):
        return self.retrieve(request ,pk)
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)
'''

'''

#Generics API View 

class EmployeView(generics.ListCreateAPIView, generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

#Generics API Details view

class EmployeDetailsView(generics.CreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView, generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'

'''

#Generics API View
class EmployeView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


#Generics Details API View
class EmployeDetailsView(generics.RetrieveUpdateDestroyAPIView, generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


#View Set 
'''
class EmployeViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Employee.objects.all()
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = EmployeeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk = None):
        queryset = get_object_or_404(Employee, pk = pk)
        serializer = EmployeeSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

        
    def update(self, request, pk=None):
        queryset = get_object_or_404(Employee, pk = pk)
        serializer = EmployeeSerializer(queryset, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk = None):
        queryset = Employee.objects.get(pk = pk)
        queryset.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)
    
'''


#Model ViewSet

class EmployeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer



#Blog Start here

class BlogView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class CommentView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


#Blog Deteils View


class BlogDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'pk'


class CommentDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'