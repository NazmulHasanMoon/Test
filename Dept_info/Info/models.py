from django.conf import settings
from django.db import models


class Student(models.Model):
    reg_roll = models.CharField(max_length=100)
    description = models.TextField()


    def __str__(self):
        return self.reg_roll