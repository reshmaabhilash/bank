from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("bankapp:add_userform")
        else:
            messages.info(request,"invalid credential")
            return redirect("credentials:login")
    return render(request,"login.html")
def register(request):
    if request.method== 'POST':
        username=request.POST['username']
        password=request.POST['password']
        confirmpassword=request.POST['cpassword']
        if password ==confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect("credentials:register")
            user=User.objects.create_user(username=username,password=password)
            user.save()
            print("user created")
            return redirect("credentials:login")
        else:
            messages.info(request,"password doesn't match")
    return render(request,"registration.html")
def logout(request):
    auth.logout(request)
    return redirect('/')