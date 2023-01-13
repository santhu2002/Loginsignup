from django.db import models

# Create your models here.


class place(models.Model):
    
    price= models.IntegerField()
    name= models.CharField(max_length=100)
