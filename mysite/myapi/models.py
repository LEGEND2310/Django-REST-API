from django.db import models

# Create your models here.


class Creator(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(max_length=1000)
    twitter = models.CharField(max_length=100)
    youtube = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    eth_address = models.CharField(max_length=50)
    charity = models.BooleanField(default=False)

    def __str__(self):
        return self.name
