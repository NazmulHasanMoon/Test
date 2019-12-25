from django.conf import settings
from django.db import models
from django.utils import timezone


class Student(models.Model):
    Id = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title