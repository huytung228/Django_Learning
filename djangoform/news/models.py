from django.db import models
from django.db.models.base import Model
from django.utils import timezone
from django import forms
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    content = models.TextField(max_length=1000)
    time_created = models.DateField()
    
    def __str__(self) -> str:
        return self.title