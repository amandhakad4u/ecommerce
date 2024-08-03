from django.db import models

# Create your models here.


# Create your models here.
class register(models.Model):

    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=128)


class users(models.Model):
    name = models.CharField(max_length=128) 
    email = models.EmailField(max_length=254, unique=True)
    dob= models.DateField()
    password = models.CharField(max_length=128)   


    




