from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import(AbstractBaseUser,BaseUserManager)

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
class UserManager(BaseUserManager):
    def create_user(self, username, password=None):

        if not username:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=self.normalize_email(username),
        )

        user.set_password(password)
        user.save()
        return user

    def create_staffuser(self, username, password):
        user = self.create_user(
            username,
            password=password,
        )
        user.staff = True
        user.save()
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            username,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save()
        return user
class User(AbstractBaseUser):
    username =models.CharField(max_length=255,unique=True)
    first_name= models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    sex=models.CharField(max_length=100)
    department=models.ForeignKey(Department,max_length=50,on_delete=models.CASCADE,default=True,blank=False,null=True)
    school=models.ForeignKey(School,max_length=50,on_delete=models.CASCADE,default=True,blank=False,null=True)
    year=models.PositiveIntegerField(null=True, blank=True)
    section=models.PositiveIntegerField(null=True, blank=True)
    active =models.BooleanField(default=True)
    staff =models.BooleanField(default=False)
    admin= models.BooleanField(default=False)

    USERNAME_FIELD='username'#username
    REQUIRED_FIELDS=[]


    def __str__(self):              # __unicode__ on Python 2
        return self.username

    objects = UserManager()
    def has_perm(self,perm, obj=None):
        return True
    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.staff
    @property
    def is_admin(self):
        return self.admin
    @property
    def is_active(self):
        return self.active
