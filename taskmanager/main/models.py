# Create your models for DB here .
from django.db import models

class Task(models.Model):
    title = models.CharField('Name', max_length=50)
    task = models.TextField('Task description')


    def __str__(self):
        return self.title

