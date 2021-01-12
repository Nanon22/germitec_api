from .general import General
from heart.models.department import Department
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Person(General):
    
    class Meta:
        verbose_name = "Person"
        ordering = ['id']

    STATUS = (
       ('admin', ('Administrator')),
       ('developer', ('Developer')),
       ('HRE', ('Humans Resources Employee')),
       ('secretary', ('Secretary')),
       ('trainee', ('Trainee')),
   )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile", null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="persons")
    status = models.CharField(max_length=32, choices=STATUS, default='trainee')

    def __str__(self):
        return self.user.username