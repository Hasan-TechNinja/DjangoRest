from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comment')
    comment = models.TextField()

    def __str__(self):
        return self.comment