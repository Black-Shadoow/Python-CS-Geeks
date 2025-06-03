from django.db import models

# Create your models here.


class Carlist(models.Model):
    name = models.CharField(max_length=50, default='Unnamed')
    desc = models.CharField(max_length=100, default='No description')
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name