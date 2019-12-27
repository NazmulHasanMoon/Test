from django.db import models
from django.conf import settings


class Student(models.Model):
    Reg = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.Reg


class Teacher(models.Model):
    Name = models.CharField(max_length=100)
    Title = models.CharField(max_length=100)
    Research_Interest = models.TextField()

    def __str__(self):
        return self.Name



