from django.shortcuts import render,redirect
# from .forms import StudentRegistrationForm
from django.contrib.auth import authenticate,login
from .models import Department,School,User
# Create your views here.

def index(request):
    return render(request, "account/index.html")
# TODO: Check PassWord Entry Again
def signup(request):
    if request.method == 'POST':
        req=request.POST
        fn=req['fname']
        ln=req['lname']
        sex=req['gender']
        un=req['usn']
        yr=req['year']
        sc=req['section']
        psw=req['psw']
        psr=req['psw-repeat']
        dep=req['dp']
        suUb=req['sub']
        dp=Department.objects.get(pk=dep)
        sb=School.objects.get(pk=suUb)
        ns=User()
        ns.username=un
        ns.first_name=fn
        ns.sex=sex
        ns.department=dp
        ns.school=sb
        ns.year=yr
        ns.section=sc
        ns.save()
    dept = Department.objects.all()
    sub = School.objects.all()
    return render(request,"registration/register.html",{"dept":dept,"sub":sub})



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
