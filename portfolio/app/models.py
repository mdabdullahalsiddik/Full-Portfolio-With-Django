from django.db import models

# Create your models here.
class About(models.Model):
    discretion = models.CharField(max_length=500)
    designation = models.CharField(max_length=50)
    designationDiscretion = models.CharField(max_length=500)
    birthDay = models.DateField( )
    websiteLink = models.URLField( max_length=1000)
    phone = models.IntegerField()
    city = models.CharField(max_length=50)
    age = models.IntegerField()
    degree = models.CharField(max_length=50)
    mail=models.EmailField( max_length=254)
    clients = models.IntegerField()
    project = models.IntegerField()
    supportHours = models.IntegerField()
    workers = models.IntegerField()
    
    
         
    
    
