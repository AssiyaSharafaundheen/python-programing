from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=30)
    place=models.CharField(max_length=50)
    phone=models.IntegerField()

    def __str__(self):
        return  self.name