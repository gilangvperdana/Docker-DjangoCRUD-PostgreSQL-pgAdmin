from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Student(models.Model):
    fullname = models.CharField(max_length=100)
    NIM = models.CharField(max_length=100)
    Mobile = models.CharField(max_length=100)
    position = models.ForeignKey(Position,on_delete=models.CASCADE)