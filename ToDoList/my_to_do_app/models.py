from django.db import models

# Create your models here. MVC - Model
class Todo(models.Model):
    content = models.CharField(max_length=255)
    isDone = models.BooleanField(default=False)