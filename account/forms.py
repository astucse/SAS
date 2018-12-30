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
# accounts.forms.py
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username',)

    def clean_email(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("username is taken")
        return username

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2


class UserAdminCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('username', 'password', 'active', 'admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
