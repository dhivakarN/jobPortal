"""jobpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('',views.landingPage,name="landingPage"),
    path('t',views.landingPage,name="loggedPage"),
    path('view/<str:company_name>',views.companyView,name="companyView"),
    path('resume',views.viewResume,name="resume"),
    path('application',views.sentApplication,name="jobApplication"),
    path('userRegister',views.userRegister,name="userRegistration"),
    # path('reg',views.userRegister,name="regi"),
    # path('hir',views.cmpnyRegister,name="cmpnyregi"),
    # path('log',views.login,name="logi"),
    # path('home1',views.emplOyee,name="home1"),
    # path('home2',views.emplOyer,name="home2"),
    # path('t',views.data,name="home3"),
    # path('r',views.uData,name="home4"),
    # path('job',views.joBs,name="JOBS"),
    # path('add',views.add,name="JOBSe"),


]
