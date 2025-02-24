from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_id = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)

    def __str__(self):
        return self.name