from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.StudentView, name='students'),
    path('studetails/<int:pk>', views.StudentDetails, name='studetails'),
    path('teacher/', views.TeacherView.as_view(), name='teachers'),
    path('teaDet/<int:pk>', views.TeacherDetails.as_view(), name='teacherDetails'),
]
