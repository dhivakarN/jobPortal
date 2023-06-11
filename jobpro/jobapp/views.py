from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
# Create your views here.

def fun(request):
    return render(request,"home.html")

def register(request):
    return render(request,"home.html")

def userRegister(request):
    a=request.POST['jsname']
    b=request.POST['jsage']
    c=request.POST['jsnumber']
    d=request.POST['jsgender']
    e=request.POST['jseducation']
    f=request.POST['jsemail']
    g=request.POST['jspassword']
    data1=employee(name=a,age=b,phNumber=c,gender=d,education=e,email=f,password=g)
    data1.save()
    return render(request,"home.html")

def cmpnyRegister(request):
    a=request.POST['jgname']
    b=request.POST['jgfield']
    c=request.POST['jgnumber']
    d=request.POST['jglocation']
    e=request.POST['jgemail']
    f=request.POST['jgpassword']
    data2=employer(cmpnyname=a, cmpnyfield=b, phNumber=c, location=d, email=e, password=f)
    data2.save()
    return render(request,"home.html")

def login(request):
    if request.method=='POST':
        lname=request.POST.get('Lname')
        pwd=request.POST.get('password')
        check_user=employee.objects.filter(name=lname,password=pwd)
        check_cmpny=employer.objects.filter(cmpnyname=lname,password=pwd)
        if check_user:
            request.session['empLoyee']=lname
            return redirect('home1')
        elif check_cmpny:
            request.session['empLoyer'] = lname
            return redirect('home2')
        else:
            return HttpResponse("wrong")


def emplOyee(request):
    if 'empLoyee' in request.session:
        return redirect('home4')

def uData(request):
    current_user = request.session['empLoyee']
    param = {'current_user': current_user}
    a=employee.objects.filter(name=current_user)
    b=employer.objects.all()
    c=jobDetail.objects.all()
    return render(request,"uProfile.html",{'data':a,'dataa':b,'daata':c})


def emplOyer(request):
    if 'empLoyer' in request.session:
        return redirect('home3')

def data(request):
    current_user = request.session['empLoyer']
    param = {'current_user': current_user}
    a=employer.objects.filter(cmpnyname=current_user)
    return render(request,"cmpnyProfile.html",{'data':a})

def joBs(request):
    return render(request,'jobs.html')

def add(request):
    a=request.POST['cmpnyNAme']
    b=request.POST['jname']
    c=request.POST['jedu']
    d=request.POST['jTime']
    e=request.POST['jsalary']
    data3=jobDetail(compnyNAme=a,jobName=b,education=c,Time=d,salary=e)
    data3.save()
    return redirect('home3')



