from django.db import models

# Create your models here.
class User(models.Model):
    Name=models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    passwd=models.CharField(max_length=30)
class Locker(models.Model):
    domain=models.CharField(max_length=256)
    username=models.CharField(max_length=30)
    email=models.ForeignKey(User,to_field='email',on_delete=models.CASCADE)
    password=models.BinaryField()
    #privatekey=models.BinaryField()