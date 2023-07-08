from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
# Create your views here.
# jobadmin typewritter
def landingPage(request):
    employerDetails=employer.objects.all()
    jobs = jobDetail.objects.all()
    return render(request,"landingPage.html",{'employer':employerDetails,'jobs':jobs})


def companyView(request,company_name = ''):
    if company_name != '':
        details = employer.objects.get(name=company_name)
        currentJobs = jobDetail.objects.filter(companyName=company_name)
    return render(request,"companyProfile.html",{'company': details , 'jobs':currentJobs})

def viewResume(request):
    return  render(request,"resume.html")

def sentApplication(request):
    name = "urte"


    return
# def testing(request):
#     return  render((request,))
def userRegister(request):
    a,b,c,d,e,f,g = "name","age","phoneNumber","gender","education","email","password"
    a=request.POST['name']
    b=request.POST['age']
    c=request.POST['phoneNumber']
    d=request.POST['gender']
    e=request.POST['education']
    f=request.POST['email']
    g=request.POST['password']
    data=employee(name=a,age=b,phoneNumber=c,gender=d,education=e,email=f,password=g)
    print(data)

    return render(request,"userProfile.html",{"data":data})

def cmpnyRegister(request):

    a=request.POST['name']
    b=request.POST['field']
    c=request.POST['number']
    d=request.POST['location']
    e=request.POST['email']
    f=request.POST['password']
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
    return render(request,"userProfile.html",{'data':a,'dataa':b,'daata':c})


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



