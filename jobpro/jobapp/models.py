from django.db import models

# Create your models here.
class employee(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    phNumber=models.IntegerField()
    gender=models.CharField(max_length=20)
    education=models.CharField(max_length=20)
    email=models.EmailField(max_length=250)
    password=models.CharField(max_length=20)

class employer(models.Model):
    cmpnyname=models.CharField(max_length=20)
    cmpnyfield=models.CharField(max_length=20)
    phNumber=models.IntegerField()
    location=models.CharField(max_length=20)
    email=models.EmailField(max_length=250)
    password=models.CharField(max_length=20)


class jobDetail(models.Model):
    compnyNAme=models.CharField(max_length=20)
    jobName=models.CharField(max_length=20)
    education=models.CharField(max_length=20)
    Time=models.CharField(max_length=20)
    salary=models.CharField(max_length=20)
