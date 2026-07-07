from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="login")
def abc(request):
    return render(request,"abc.html")

@login_required(login_url="login")
def led(request):
    return render(request,"led.html")

@login_required(login_url="login")
def index(request):
    return render(request,"index.html")

@login_required(login_url="login")
def Counter(request):
    if(request.method=="POST"):
        data=request.POST
        result=data.get('result')
        if result=="":
            result=0
        else:
            result=int(data.get("result"))

        if('increment' in request.POST):
            result=result+1
            return render(request,"Counter.html",context={'result':result})

        if('decrement' in request.POST):
            result=result-1
            return render(request,"Counter.html",context={'result':result})

        if('reset' in request.POST):
            result=0
            return render(request,"Counter.html",context={'result':result})


    return render(request,"Counter.html")


@login_required(login_url="login")
def calci(request):
    if(request.method=="POST"):
        data=request.POST
        first=int(data.get('firstnumber'))
        second=int(data.get('secondnumber'))

        if('add'in request.POST):
            result=first+second
            return render(request,"calci.html",context={'result':"sum="+str(result)})

        if('sub'in request.POST):
            result=first-second
            return render(request,"calci.html",context={'result':"sub="+str(result)})

        if('mul'in request.POST):
            result=first*second
            return render(request,"calci.html",context={'result':"mul="+str(result)})

        if('div'in request.POST):
            result=first/second
            return render(request,"calci.html",context={'result':"div="+str(result)})
    return render(request,"calci.html")

@login_required(login_url="login")
def Employee(request):
    if(request.method=="POST"):
        data=request.POST
        empname=data.get('employeename')
        empdes=data.get('employeedes')
        empplace=data.get('employeeplace')
        Employee_table.objects.create(EMP_NAME=empname,EMP_DES=empdes,EMP_Place=empplace)
        result="Employee Details Saved!!"
        return render(request,"Employee.html",context={'result':result})
    return render(request,"Employee.html")
        

@login_required(login_url="login")        
def Employee_View(request):
    getEmployee=Employee_table.objects.all()
    return render(request,"Employee_View.html",context={'getEmployee':getEmployee})


@login_required(login_url="login")
def Employee_update(request,id):
    getEmployee=Employee_table.objects.get(id=id)
    if(request.method=="POST"):
        data=request.POST
        empname=data.get('employeename')
        empdes=data.get('employeedes')
        empplace=data.get('employeeplace')
        getEmployee.EMP_NAME=empname
        getEmployee.EMP_DES=empdes
        getEmployee.EMP_Place=empplace
        getEmployee.save()
        return redirect('/Employee_View/')
    return render(request,"Employee_update.html",context={'getEmployee':getEmployee})


@login_required(login_url="login")
def Employee_delete(request,id):
    getEmployee=Employee_table.objects.get(id=id)
    if(request.method=="POST"):
        data=request.POST
        getEmployee.delete()
        return redirect('/Employee_View/')
    return render(request,'Employee_delete.html',context={'getEmployee':getEmployee})

def SignupPage(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("Your password and confirm password are not same!!")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render(request,"signup.html")

def LoginPage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=User.objects.filter(username=username)
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return HttpResponse("Username or Password is Incorrect!!")
    return render(request,'login.html')

def Logoutpage(request):
    logout(request)
    return redirect('login')