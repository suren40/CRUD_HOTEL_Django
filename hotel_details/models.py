from django.db import models

# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=400)
    url = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.name
