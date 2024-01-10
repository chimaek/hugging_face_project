from django.db import models
from django.db.models import Model


# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return self.name