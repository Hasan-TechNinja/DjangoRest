from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.StudentView, name='students'),
    path('studetails/<int:pk>', views.StudentDetails, name='studetails'),
    path('teacher/', views.TeacherView.as_view(), name='teachers'),
    path('teaDet/<int:pk>', views.TeacherDetails.as_view(), name='teacherDetails'),
    path('employes/', views.EmployeView.as_view(), name='employe'),
    path('empDets/<int:pk>', views.EmployeDetailsView.as_view(), name='employe'),
]
