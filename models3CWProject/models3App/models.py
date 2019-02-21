from django.db import models

# Create your models here.
from django.db import models

# Book class with elements
class Book(models.Model):
    name = models.CharField(max_length=10000)
    pageNumber = models.IntegerField(default=0)
    genre = models.CharField(max_length=30)
    publishDate = models.DateField()

    def __str__(self):
        return self.name
