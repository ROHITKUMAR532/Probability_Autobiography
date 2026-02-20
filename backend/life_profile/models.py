from django.db import models

class LifeProfile(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    profession = models.CharField(max_length=100)
    probability = models.IntegerField(default=0)

    def __str__(self):
        return self.name
from django.db import models

class LifeProfile(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    profession = models.CharField(max_length=100)
    probability = models.IntegerField()

    def __str__(self):
        return self.name