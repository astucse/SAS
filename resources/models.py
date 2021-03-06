from django.db import models
from django.contrib.auth.models import User
from account.models import Subject,Department
# Create your models here.

class Slide(models.Model):
    file=models.CharField(max_length=256)
    name=models.CharField(max_length=55)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE,related_name="sub")
    department=models.ForeignKey(Department,on_delete=models.CASCADE,related_name="dept")
    def __str__(self):
        return self.name

class Handout(models.Model):
    name=models.CharField(max_length=55,blank=True)
    file=models.CharField(max_length=256)
    section=models.IntegerField()
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Question(models.Model):
    question_text=models.TextField()
    chapter=models.PositiveIntegerField(null=True)
    type=models.CharField(max_length=50,choices=(('Multiple Choice','MC'),('Short Answer','SA'),('True or False','TF'),('Fill in the blanks','FITB'),('Flash Card','FC')))
    explanation=models.TextField()
    hint=models.TextField()
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    date_uploaded=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.question_text[:15]

class Choice(models.Model):
    choice_text=models.TextField()
    question=models.ForeignKey(Question,on_delete=models.CASCADE,related_name='choices')
    answer_to=models.ForeignKey(Question,on_delete=models.CASCADE,related_name='answer',null=True)
    def __str__(self):
        return self.choice_text

class Exam(models.Model):
    name=models.CharField(max_length=55,blank=True)
    url=models.CharField(max_length=250)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Video(models.Model):
    url=models.CharField(max_length=250,blank=True)
    name=models.CharField(max_length=100)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE,null=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.name
