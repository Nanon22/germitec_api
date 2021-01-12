from django.db import models
from django.utils import timezone

class General(models.Model):
    
    deleted = models.BooleanField(default=False)
    date_added = models.DateTimeField(default=timezone.now)