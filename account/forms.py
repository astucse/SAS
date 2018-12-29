# from django.contrib.auth.models import User
# from django.db import models
# from .models import Department,School
# from django.contrib.auth.forms import UserCreationForm
# class StudentRegistrationForm(UserCreationForm):
#     student_id=models.CharField(max_length=12)
#     first_name=models.CharField(max_length=50)
#     last_name=models.CharField(max_length=50)
#     department=models.OneToOneField(Department,max_length=50,on_delete=models.CASCADE)
#     year=models.PositiveIntegerField()
#     school=models.OneToOneField(School,on_delete=models.CASCADE)
#     avatar=models.ImageField(blank=True,upload_to='',default='null.png')
#
#     class Meta:
#         model = User
#         fields = {'student_id','first_name','last_name','department','year','school','avatar','username','password1','password2','email'}
#
#     def save(self,commit=True):
#         user = super(StudentRegistrationForm,self).save(commit=False)
#         user.student_id = cleaned_data["student_id"]
#         user.first_name = cleaned_data["first_name"]
#         user.last_name = cleaned_data["last_name"]
#         user.email = cleaned_data["email"]
#         user.department=cleaned_data["department"]
#         user.year=cleaned_data["year"]
#         user.school=cleaned_data["school"]
#         user.avatar=cleaned_data["avatar"]
#         if commit:
#             user.save()
#         return user
