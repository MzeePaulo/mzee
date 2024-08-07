from django.db import models

# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.firstname+" "+self.lastname


class Services(models.Model):
    name = models.CharField(max_length=50)
    cost = models.IntegerField(default=0)
    description = models.TextField()

    def __str__(self):
        return self.name

class DesignModel(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    price = models.CharField(max_length=50)

    def __str__(self):
        return self.title

