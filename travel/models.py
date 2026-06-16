from django.db import models
from django.contrib.auth.models import User

class Destination(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    img = models.ImageField(upload_to='pics')
    offer = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Request(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)    

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    destination = models.ForeignKey('Destination', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.destination.name}"