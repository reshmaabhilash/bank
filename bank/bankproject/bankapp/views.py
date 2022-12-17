from django.shortcuts import render,redirect
from .models import District,Branch,Userform
from .forms import BankForm
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
            return redirect("bankapp:login")
    return render(request,"login.html")
def register(request):
    if request.method== 'POST':
        username=request.POST['username']
        password=request.POST['password']
        confirmpassword=request.POST['cpassword']
        if password ==confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')
            user=User.objects.create_user(username=username,password=password)
            user.save()
            print("user created")
            return redirect('login')
        else:
            messages.info(request,"password doesn't match")
    return render(request,"registration.html")
def logout(request):
    auth.logout(request)
    return redirect('/')

# Create your views here.
def Regform(request):
    return render(request,'home.html')
def index(request):
    form=Userform.objects.all()
    context={
        'form_list':form
    }
    return render(request,'index.html',context)
# def add_userform(request):
#     if request.method=="POST":
#         name = request.POST.get('name', )
#         age = request.POST.get('age', )
#         phonenumber = request.POST.get('phonenumber', )
#         email= request.POST.get('email', )
#         address=request.POST.get('address', )
#         district=request.POST.get('district', )
#         branch=request.POST.get('branch', )
#         userform=Userform(name=name,age=age,phonenumber=phonenumber,email=email,address=address,district=district,branch=branch)
#         userform.save()
#     return render(request,'userform.html')
def add_userform(request):
    form=BankForm()
    if request.method=='POST':
        form=BankForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("bankapp:login")
    return render(request,"userform.html",{'form':form})