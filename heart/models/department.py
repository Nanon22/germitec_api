from django.db import models
from .general import General

class Department(General):
    
    class Meta:
        verbose_name = "Department"
        ordering = ['id', 'name']

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name