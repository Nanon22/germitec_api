from django.db import models
from django.utils import timezone

class Department(models.Model):
    
    class Meta:
        verbose_name = "Department"
        ordering = ['id', 'name']

    name = models.CharField(max_length=255)
    deleted = models.BooleanField(default=False)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name