from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser
# Create your models here.


class regsitration(models.Model):
    LOGIN_TYPE_CHOICES = [
        ('user', 'User'),
        ('admin', 'Admin'),
        ('business', 'Business'),
    ]
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    login_type=models.CharField(max_length=255, choices=LOGIN_TYPE_CHOICES, default='')

    def __str__(self):
        return self.username


class CustomUser(AbstractUser):
    REQUIRED_FIELDS = ['account_type']  # Add other required fields as needed
    ACCOUNT_CHOICES = [
        ('user', 'User'),
        ('admin', 'Admin'),
        ('business', 'Business'),
    ]

    BUSINESS_CHOICES = [
        ('hotel', 'Hotel'),
        ('restaurant', 'Restaurant'),
        ('hospital', 'Hospital'),
        ('mini-industry', 'Mini Industry'),
        ('others', 'Others'),
    ]

    account_type = models.CharField(max_length=10, choices=ACCOUNT_CHOICES,default='User')
    full_name = models.CharField(max_length=255)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=256)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length = 254)
    business_type = models.CharField(max_length=15, choices=BUSINESS_CHOICES, default='',)
    other_business_text = models.CharField(max_length=255, default='',)
    USERNAME_FIELD = 'username'


    def __str__(self):
        return self.username


class complain(models.Model):
    full_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15,default='')
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to=r"C:\Users\soham\Downloads\EcoSathi\EcoSathi\Complain photo", null=True, blank=True)   #upload_to='services_images/',
    created_at = models.DateTimeField(auto_now_add=True)
    account_type = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.full_name


class PickupBooking(models.Model):
    companyName = models.CharField(max_length=255)
    userName = models.CharField(max_length=255)
    address = models.TextField(max_length=100)
    phone_number = models.CharField(max_length=15)
    pickupDate = models.DateField()
    pickupTime = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.companyName} - {self.userName}"
    

class Dustbin(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()