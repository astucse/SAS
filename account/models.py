from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class School(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Department(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    school=models.ForeignKey(School,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class Subject(models.Model):
    name=models.CharField(max_length=50)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    student_id=models.CharField(max_length=12)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    department=models.OneToOneField(Department,max_length=50,on_delete=models.CASCADE)
    year=models.PositiveIntegerField()
    school=models.OneToOneField(School,on_delete=models.CASCADE)
    avatar=models.ImageField(blank=True,upload_to='',default='null.png')
    def __str__(self):
        return self.first_name
class Teacher(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    username=models.CharField(max_length=12)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    department=models.OneToOneField(Department,max_length=50,on_delete=models.CASCADE)
    avatar=models.ImageField(blank=True,upload_to='',default='null.png')
    def __str__(self):
        return self.first_name
