from django.db import models

# Create your models here.
class employee(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    phoneNumber=models.IntegerField()
    gender=models.CharField(max_length=20)
    education=models.CharField(max_length=20)
    email=models.EmailField(max_length=250)
    password=models.CharField(max_length=20)

class employer(models.Model):
    name=models.CharField(max_length=20)
    field=models.CharField(max_length=20)
    phoneNumber=models.IntegerField()
    location=models.CharField(max_length=20)
    email=models.EmailField(max_length=250)
    password=models.CharField(max_length=20)


class jobDetail(models.Model):
    companyName=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    education=models.CharField(max_length=20)
    Time=models.CharField(max_length=20)
    salary=models.CharField(max_length=20)

class Fileupload(models.Model):
    name = models.CharField(max_length=20)
    file = models.FileField(upload_to = 'media/')