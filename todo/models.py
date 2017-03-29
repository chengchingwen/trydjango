from django.db import models

# Create your models here.

class TodoTask(models.Model):
    title = models.CharField(max_length=256)
    detail =models.TextField(null=True)
    done = models.BooleanField(default=False)
    dead_line = models.DateTimeField(null=True)
    
