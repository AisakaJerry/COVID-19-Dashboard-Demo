from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

class PersonalInfo(models.Model):
    name = models.CharField(max_length=100)
    gender = models.BooleanField()
    age = models.CharField(max_length=10)

    def __str__(self):
        return self.name