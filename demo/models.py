from django.db import models

# Create your models here.
class person(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    gender=models.CharField(max_length=20)
    height=models.FloatField()
    weight=models.FloatField()
    email=models.EmailField(unique=True)
    phone=models.BigIntegerField(unique=True)
    address=models.CharField(max_length=40,default="null")



