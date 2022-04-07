from django.db import models

# Create your models here.

class Neighbourhood(models.Model):
    name= models.CharField(max_length=200, null = True, blank=False)
    country = models.CharField(max_length=200, null = True, blank=False)
    city = models.CharField(max_length=200, null = True, blank=False)
    image = models.ImageField(blank=True, null = True)

    def __str__(self) :
        return self.name

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
    neighbourhood = models.ForeignKey(Neighbourhood, null = True, on_delete=models.DO_NOTHING) 
    name = models.CharField(max_length=200, null =True)
    price = models.FloatField(default = 0.0)
    category= models.CharField(max_length=200, choices = CATEGORY, null = True)
    description = models.CharField(max_length=200, null=True, blank= True)
    datecreated = models.DateTimeField(auto_now_add=True, null=True)
    image = models.ImageField(blank=True, null = True)

    def __str__(self):
        return self.name

class Event(models.Model):
    #organizer = models.ForeignKey(NewUser, null=True, on_delete=models.DO_NOTHING)
    neighbourhood = models.ForeignKey(Neighbourhood, null = True, on_delete=models.DO_NOTHING) 
    name = models.CharField(max_length=200, null= True)
    time = models.TimeField(null = True)
    date = models.DateField(null =True)
    place = models.CharField(max_length=200, null = True)
    participantsnumb =models.IntegerField(null=True)
    maxparticipants = models.IntegerField(null= True)
    image = models.ImageField(blank=True, null = True)

    def __str__(self):  
        return self.name

class Facility(models.Model):
    name = models.CharField(max_length=200, null= True)
    neighbourhood = models.ForeignKey(Neighbourhood,null=True, on_delete=models.DO_NOTHING) 
    Address = models.CharField(max_length=200, null = True)
    Phone = models.CharField(max_length=8, null = True)
    datecreated= models.DateTimeField(auto_now_add=True, null=True)  
    image = models.ImageField(blank=True, null = True)

    def __str__(self) :
        return self.name

class Article(models.Model):
    #writer = models.ForeignKey(NewUser, null = True, on_delete=models.SET_NULL)
    neighbourhood = models.ForeignKey(Neighbourhood, null = True, on_delete=models.DO_NOTHING) 
    datecreated = models.DateTimeField(auto_now_add=True, null = True)
    title = models.CharField(max_length=200, null = True, blank= False,)
    text =  models.TextField(max_length=1000, null = True, blank = False, default='text')
    likes = models.IntegerField(null = True, default=0)

class Job(models.Model):
    #user = models.ForeignKey(NewUser, null =True, on_delete=models.DO_NOTHING, )
    neighbourhood = models.ForeignKey(Neighbourhood, null = True, on_delete=models.DO_NOTHING, default='Ras Beirut') 
    title = models.CharField(max_length=200, null = True, blank = False)
    description = models.TextField(max_length=1000, null = True, blank= False)
    Address = models.CharField(max_length=200, null= True, blank = False)
    datecreated = models.DateTimeField(auto_now_add=True, null = True)
    pay = models.CharField(max_length=200, null = True)

