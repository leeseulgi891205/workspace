from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    age = models.IntegerField()
    grade = models.IntegerField()
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    hobby = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='student_images/', blank=True, null=True)
    
    def __str__(self):
        return self.name
