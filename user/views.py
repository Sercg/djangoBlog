from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages


# Create your views here.

def register(request):

    form = RegisterForm(request.POST or None)

    if form.is_valid(): #calls clean method from RegisterForm
        
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password") 
        
        user=User(username=username)
        user.set_password(password)
        
        user.save()
        login(request,user)
        messages.success(request,"You are registered successfully")
        
        return redirect("index")
    context ={"form" : form}
    return render(request,"register.html",context)
    
def loging(request):

    form = LoginForm(request.POST or None)
    context = {"form":form}

    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user =authenticate(username=username, password=password)

        if user is None:
            messages.info(request,"Wrong password or username")
            return render(request,"login.html",context)

        messages.success(request,"Successfully logged in")
        login(request,user)
        return redirect("index")

    return render(request, "login.html",context)

def logingout(request):
    logout(request)
    messages.success(request,"Successfully logged out")
    return redirect("index")