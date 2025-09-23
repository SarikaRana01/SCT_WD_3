from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from  django.contrib import messages


def signUp_view(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        confirm_password=request.POST.get("confirm_password")
        if username==None:
            messages.warning(request,"Username can't be empty")
            return redirect("signUp")
        if password==None:
            messages.warning(request,"Password can't be empty")
            return redirect("signUp")

        if password != confirm_password:
            messages.error(request,"Password do not match")
            return redirect("signUp")
        temp=authenticate(request,username=username,password=password)
        if temp is not None:
            messages.warning(request,"Account already exits")
            return render("signUp")
        user=User.objects.create(username=username)
        user.set_password(password)
        user.save()
        login(request,user)
        messages.success(request,"Account created successfully")
        return redirect("CategoryDisplay")
    return render(request,"Accounts/signUp.html")


def login_view(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Logged in successfully")
            return redirect("CategoryDisplay")
        else:
            messages.error(request,"Account not exists")
    return render(request,"Accounts/login.html")



def logout_view(request):
    logout(request)
    messages.success(request,"Logged out successfully")
    return redirect("login")