from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employee', views.EmployeViewSet, basename='employeee')

urlpatterns = [
    path('students/', views.StudentView, name='students'),
    path('studetails/<int:pk>', views.StudentDetails, name='studetails'),
    path('teacher/', views.TeacherView.as_view(), name='teachers'),
    path('teaDet/<int:pk>', views.TeacherDetails.as_view(), name='teacherDetails'),
    path('employess/', views.EmployeView.as_view(), name='employe'),
    path('empDets/<int:pk>', views.EmployeDetailsView.as_view(), name='employe'),
    path('', include(router.urls ))
]
