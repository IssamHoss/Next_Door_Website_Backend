from datetime import *
from distutils.command.upload import upload
import email
from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager,  PermissionsMixin
from nxtdor2 import settings

# Create your models here.

class Neighbourhood(models.Model):
    name= models.CharField(max_length=200, null = False, blank=False, default=  "")
    country = models.CharField(max_length=200, null = False, blank=False, default=  "")
    city = models.CharField(max_length=200, null = False, blank=False, default=  "")

    def __str__(self) :
        return self.name+" , "+self.country+" , "+self.city

class MyAccountManager(BaseUserManager):

    def create_user(self, email, username, name, password , **other_fields):
        email = self.normalize_email(email)
        user = self.model(email = email, username = username , name = name, **other_fields )
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, username, name, password , **kwargs):
        user = self.create_user(
            email = email,
            username= username,
            name= name,
            password= password,
            is_superuser=True,
            is_staff = True,
            is_admin = True,
            **kwargs
        )


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='email', max_length= 60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=30, null =False , blank = False, default ="john Doe")
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active= models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    neighbourhood = models.ForeignKey(Neighbourhood, null = True, on_delete=models.CASCADE)
    profile_image = models.ImageField(null =True, blank =True, upload_to= 'pimages/', default='pimages/def_user.png')

    objects= MyAccountManager()
    USERNAME_FIELD =  'email'
    REQUIRED_FIELDS =  ['username', 'name']
    


class Product(models.Model):
    CATEGORY = (
            ('Vehicle' , 'Vehicle'),
            ('Furniture', 'Furniture'),
            ('Clothes', 'Clothes'),
            ('Shoes', 'Shoes'),
            ('Electronics', 'Electronics'),
            ('Toys', 'Toys'),
            ('Kitchen Appliances', 'Kitchen Appliances'),
            ('Sport\'s Equipment', 'Sport\'s Equipment'),
            ('Education', 'Education'),
            )

    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbourhood, null = True, default=  "", on_delete=models.CASCADE) 
    name = models.CharField(max_length=200,  null = False, blank=False, default=  "")
    price = models.FloatField(default = 0.0)
    category= models.CharField(max_length=200, choices = CATEGORY, null = False, blank=False, default="Vehicle")
    description = models.CharField(max_length=200, null = False, blank=True, default=  "")
    date = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(null =True, blank =True, upload_to= 'productimages/')

    def __str__(self):
        return self.name

class Event(models.Model):
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbourhood, null = True, default=  "", on_delete=models.CASCADE) 
    name = models.CharField(max_length=200,  null = False, blank=False, default=  "null")
    timeanddate = models.CharField(max_length= 100, null = False, default ="")
    place = models.CharField(max_length=200, null = False, default ="")
    image = models.ImageField(null =True, blank =True, upload_to= 'eventimages/')

    def __str__(self):  
        return self.name

class Facility(models.Model):
    name = models.CharField(max_length=200,  null = False, blank=False, default=  "")
    neighbourhood = models.ForeignKey(Neighbourhood,null=True, default ="",on_delete=models.CASCADE) 
    Address = models.CharField(max_length=200, null = False, default ="")
    Phone = models.CharField(max_length=8, null = False, default ="")
    datecreated = models.DateTimeField(auto_now_add = True) 
    image = models.ImageField(null =True, blank =True, upload_to= 'facilityimages/')

    def __str__(self) :
        return self.name

class Article(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbourhood, null =True, default ="", on_delete=models.CASCADE) 
    datecreated = models.DateTimeField(auto_now_add = True)
    title = models.CharField(max_length=200,  null = False, blank=False, default=  "")
    text =  models.TextField(max_length=1000, null = False, blank = False, default='')


    def __str__(self) :
        return self.title

class Job(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbourhood, null = True, default ="", on_delete=models.CASCADE) 
    title = models.CharField(max_length=200,  null = False, blank=False, default=  "")
    description = models.TextField(max_length=1000, null = False, default ="", blank= False)
    address = models.CharField(max_length=200, null= False, blank = False, default = "")
    datecreated = models.DateTimeField(auto_now_add = True)
    pay = models.CharField(max_length=200, null = False, default ="")

    def __str__(self) :
        return self.title