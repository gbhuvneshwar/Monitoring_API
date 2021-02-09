from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class Devices(models.Model):
    """Database model for N number of devices"""

    device_name = models.CharField(max_length=100,blank=True,null=True)
    device_status = models.BooleanField(default=False)
    cpu_utilization = models.CharField(max_length=100,blank=True,null=True)
    memory_utilization =  models.CharField(max_length=1000,blank=True,null=True)


    def __str__(self):              
        return self.device_name


class UserProfile(AbstractBaseUser):
    """Database model for user in system"""
    username = None
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):              
        return self.email   