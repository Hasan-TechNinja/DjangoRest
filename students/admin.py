from django.contrib import admin
from . models import Students

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'student_id', 'name', 'branch'
    )
admin.site.register(Students, StudentAdmin)