from django.db import models
import uuid

class Article(models.Model):
    name = models.CharField(max_length=100, unique=True)
    author = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
