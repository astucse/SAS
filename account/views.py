from django.shortcuts import render,redirect
# from .forms import StudentRegistrationForm
from django.contrib.auth import authenticate,login

# Create your views here.

def index(request):
    return render(request, "account/index.html")
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
