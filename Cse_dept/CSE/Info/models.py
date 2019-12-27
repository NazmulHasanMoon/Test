from django.db import models
from django.conf import settings


class Student(models.Model):
    Reg = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.Reg