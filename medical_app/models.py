from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    is_patient=models.BooleanField(default=False)
    is_doctor=models.BooleanField(default=False)

class Profile(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    profile_picture=models.ImageField(upload_to='profile_pic/',blank=True,null=True)
    address_line1=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    pincode=models.CharField(max_length=6)
class Patient(models.Model):
    profile=models.OneToOneField(Profile,on_delete=models.CASCADE)

class Docter(models.Model):
    profile=models.OneToOneField(Profile,on_delete=models.CASCADE)
