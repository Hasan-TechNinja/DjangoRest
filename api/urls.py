from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.StudentView, name='students'),
    path('studetails/<int:pk>', views.StudentDetails, name='studetails'),
]
