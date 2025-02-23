from django.db import models

# Create your models here.

class Teacher(models.Model):
    teacher_id = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=200)
    joinDate = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}, {self.location}"
