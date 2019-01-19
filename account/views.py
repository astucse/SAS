from django.shortcuts import render,redirect
# from .forms import StudentRegistrationForm
from django.contrib.auth import authenticate,login,logout
from .models import Department,School,User,Profile
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.
@login_required
def index(request):
    if(request.method=='POST'):
            logout(request)
            return render(request,"account/index.html")
    return render(request, "account/index.html")
# TODO: Clean Password
def signup(request):
    if request.method == 'POST':
        req=request.POST
        fn=req['firstname']
        ln=req['lastname']
        sex=req['gender']
        un=req['username']
        yr=req['year']
        sc=req['section']
        psw=req['Password']
        dep=req['dp']
        suUb=req['sub']
        dp=Department.objects.get(pk=dep)
        sb=School.objects.get(pk=suUb)
        user=User()
        user.username=un
        user.first_name=fn
        user.last_name=ln
        user.set_password(psw)
        user.save()
        user_profile=User.objects.get(username=un)
        user_profile.profile.sex=sex
        user_profile.profile.department=dp
        user_profile.profile.school=sb
        user_profile.profile.year=yr
        user_profile.profile.section=sc
        user_profile.save()
    dept = Department.objects.all()
    sub = School.objects.all()
    return render(request,"registration/Signup.html",{"dept":dept,"sub":sub})
def test(request):
    x="--"
    if(request.method=='POST'):
        req=request.POST
        if req['b']=="Login":
            un=req['username']
            pw=req['password']
            user=authenticate(username=un,password=pw)
            if user is not None:
                login(request,user)
                return render(request,"registration/test.html")
            else:
                x="Wrong Username Or Password"
                return render(request,"registration/test.html",{x:x})
        else:
            logout(request)
            return render(request,"registration/test.html")
    return render(request,"registration/test.html",{x:x})


# def register(request):
#     if request.method == 'POST':
#         form=StudentRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username=form.cleaned_data['username']
#             password=form.cleaned_data['password1']
#             user=authenticate(username=username,password=password)
#             login(request,user)
#             return redirect('index')
#     else:
#         form=UserCreationForm()
#     context={'form': form}
#     return render(request, 'registration/register.html',context)
