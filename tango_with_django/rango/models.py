from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

class Page(models.Model):
    Category = models.ForeignKey(Category)
    tittle = models.CharField(max_length=128)
    Url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.tittle
