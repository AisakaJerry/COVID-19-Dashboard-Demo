from django.db import models

# Create your models here.
class Takeout(models.Model):
    restaurant_name=models.CharField(max_length=200)
    dishes=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.restaurant_name