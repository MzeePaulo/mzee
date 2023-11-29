from django.db import models

# Create your models here.
class Services(models.Model):
    name = models.CharField(max_length=50)
    cost = models.IntegerField(default=0)
    description = models.TextField()

    def __str__(self):
        return self.name