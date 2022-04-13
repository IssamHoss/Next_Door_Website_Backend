from datetime import *
from email.policy import default
from django.db import models

# Create your models here.

class Neighbourhood(models.Model):
    name= models.CharField(max_length=200, null = False, blank=False, default=  "")
    country = models.CharField(max_length=200, null = False, blank=False, default=  "")
    city = models.CharField(max_length=200, null = False, blank=False, default=  "")

    def __str__(self) :
        return self.name+" , "+self.country+" , "+self.city

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

    #seller = models.ForeignKey(NewUser, null= True,on_delete = models.DO_NOTHING)
    neighbourhood = models.ForeignKey(Neighbourhood, null = True, default=  "", on_delete=models.CASCADE) 
    name = models.CharField(max_length=200,  null = False, blank=False, default=  "")
    price = models.FloatField(default = 0.0)
    category= models.CharField(max_length=200, choices = CATEGORY, null = False, blank=False, default="Vehicle")
    description = models.CharField(max_length=200, null = False, blank=True, default=  "")
    date = models.DateTimeField(auto_now_add = True)

    #image = models.ImageField(blank=True, null = False)

    def __str__(self):
        return self.name

class Event(models.Model):
    #organizer = models.ForeignKey(NewUser, null=True, on_delete=models.DO_NOTHING)
    neighbourhood = models.ForeignKey(Neighbourhood, null = True, default=  "", on_delete=models.CASCADE) 
    name = models.CharField(max_length=200,  null = False, blank=False, default=  "null")
    timeanddate = models.CharField(max_length= 100, null = False, default ="")
    place = models.CharField(max_length=200, null = False, default ="")
    participantsnumb =models.IntegerField(null=True)
    maxparticipants = models.IntegerField(null= True)
    #image = models.ImageField(upload_to='profile_pic', default='default.jpg')

    def __str__(self):  
        return self.name

class Facility(models.Model):
    name = models.CharField(max_length=200,  null = False, blank=False, default=  "")
    neighbourhood = models.ForeignKey(Neighbourhood,null=True, default ="",on_delete=models.CASCADE) 
    Address = models.CharField(max_length=200, null = False, default ="")
    Phone = models.CharField(max_length=8, null = False, default ="")
    datecreated = models.DateTimeField(auto_now_add = True) 
    #image = models.ImageField(blank=True, null = False, default =)

    def __str__(self) :
        return self.name

class Article(models.Model):
    #writer = models.ForeignKey(NewUser, null = False, default =, on_delete=models.SET_NULL)
    neighbourhood = models.ForeignKey(Neighbourhood, null =True, default ="", on_delete=models.CASCADE) 
    datecreated = models.DateTimeField(auto_now_add = True)
    title = models.CharField(max_length=200,  null = False, blank=False, default=  "")
    text =  models.TextField(max_length=1000, null = False, blank = False, default='')
    likes = models.IntegerField(null = False, default=0)

    def __str__(self) :
        return self.title

class Job(models.Model):
    #user = models.ForeignKey(NewUser, null =True, on_delete=models.DO_NOTHING, )
    neighbourhood = models.ForeignKey(Neighbourhood, null = True, default ="", on_delete=models.CASCADE) 
    title = models.CharField(max_length=200,  null = False, blank=False, default=  "")
    description = models.TextField(max_length=1000, null = False, default ="", blank= False)
    address = models.CharField(max_length=200, null= False, blank = False, default = "")
    datecreated = models.DateTimeField(auto_now_add = True)
    pay = models.CharField(max_length=200, null = False, default ="")

    def __str__(self) :
        return self.title