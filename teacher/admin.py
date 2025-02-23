from django.contrib import admin
from . models import Teacher

# Register your models here.

class TeacherAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'teacher_id', 'name', 'location', 'joinDate', 'status'
    )
admin.site.register(Teacher, TeacherAdmin)