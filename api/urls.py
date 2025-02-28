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
    path('', include(router.urls )),

    path('blog/', views.BlogView.as_view(), name='blog'),
    path('comment/', views.CommentView.as_view(), name='comment'),
    path('blogDetails/<int:pk>', views.BlogDetailsView.as_view(), name='blogDetails'),
    path('commentDetails/<int:pk>', views.CommentDetailsView.as_view(), name='commentDetails')
]
