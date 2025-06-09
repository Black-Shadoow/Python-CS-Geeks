from django.db import models

# Create your models here.


from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from django.db import models

# Create your models here.
from django.db import models
class Showroom(models.Model):  # Capital S
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Carlist(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    def __str__(self):
        return self.name
class Review(models.Model):
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comments = models.CharField(max_length=100, null=True)
    car = models.ForeignKey(Carlist, on_delete=models.CASCADE, related_name="reviews", null=True)
    created = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)

    def __str__(self):
        return f"The rating of car {self.car.name} --- {self.rating}"