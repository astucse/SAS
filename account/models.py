from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import(AbstractBaseUser,BaseUserManager)
from django.db.models.signals import post_save
from django.dispatch import receiver
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
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_no=models.CharField(max_length=40,default="aur")
    sex=models.CharField(max_length=100)
    department=models.ForeignKey(Department,max_length=50,on_delete=models.CASCADE,default=True,blank=False,null=True)
    school=models.ForeignKey(School,max_length=50,on_delete=models.CASCADE,default=True,blank=False,null=True)
    year=models.PositiveIntegerField(default=True,blank=False)
    section=models.PositiveIntegerField(default=True,blank=False,null=True)
    def __str__(self):
        return self.user.first_name
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# class Student(models.Model):
#     user=models.OneToOneField(User,on_delete=models.CASCADE)
#     student_id=models.CharField(max_length=12)
#     first_name=models.CharField(max_length=50)
#     last_name=models.CharField(max_length=50)
#     department=models.OneToOneField(Department,max_length=50,on_delete=models.CASCADE)
#     year=models.PositiveIntegerField()
#     school=models.OneToOneField(School,on_delete=models.CASCADE)
#     avatar=models.ImageField(blank=True,upload_to='',default='null.png')
#     def __str__(self):
#         return self.first_name
# class Teacher(models.Model):
#     user=models.OneToOneField(User,on_delete=models.CASCADE)
#     username=models.CharField(max_length=12)
#     first_name=models.CharField(max_length=50)
#     last_name=models.CharField(max_length=50)
#     department=models.OneToOneField(Department,max_length=50,on_delete=models.CASCADE)
#     avatar=models.ImageField(blank=True,upload_to='',default='null.png')
#     def __str__(self):
#         return self.first_name
#=========================================== USER ======================================
# class UserManager(BaseUserManager):
#     def create_user(self, username, password):
#
#         if not username:
#             raise ValueError('Users must have an Username')
#
#         user = self.model(
#             username=self.normalize_email(username),
#         )
#
#         user.set_password(password)
#         user.save()
#         return user
#
#     def create_staffuser(self, username, password):
#         user = self.create_user(
#             username,
#             password=password,
#         )
#         user.staff = True
#         user.save()
#         return user
#
#     def create_superuser(self, username, password):
#         user = self.create_user(
#             username,
#             password=password,
#         )
#         user.staff = True
#         user.admin = True
#         user.save()
#         return user
# class User(AbstractBaseUser):
#     username =models.CharField(max_length=255,unique=True)
#     first_name= models.CharField(max_length=100,default=True,blank=False,null=True)
#     last_name= models.CharField(max_length=100,default=True,blank=False,null=True)
#     sex=models.CharField(max_length=100,default=True,blank=False,null=True)
#     department=models.OneToOneField(Department,max_length=50,on_delete=models.CASCADE,default=True,blank=False,null=True)
#     school=models.OneToOneField(School,max_length=50,on_delete=models.CASCADE,default=True,blank=False,null=True)
#     year=models.PositiveIntegerField(default=True,blank=False,null=True)
#     section=models.PositiveIntegerField(default=True,blank=False,null=True)
#     active =models.BooleanField(default=True)
#     staff =models.BooleanField(default=False)
#     admin= models.BooleanField(default=False)
#
#     USERNAME_FIELD='username'#username
#     REQUIRED_FIELDS=[]
#
#
#     def __str__(self):              # __unicode__ on Python 2
#         return self.username
#
#     objects = UserManager()
#     def has_perm(self,perm, obj=None):
#         return True
#     def has_module_perms(self,app_label):
#         return True
#
#     @property
#     def is_staff(self):
#         return self.staff
#     @property
#     def is_admin(self):
#         return self.admin
#     @property
#     def is_active(self):
#         return self.active
