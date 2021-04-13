from django.db import models
from django.db.models.base import Model
from django import forms

# Create your models here.
class Takeout(models.Model):
    restaurant_name=models.CharField(max_length=200)
    dishes=models.TextField()
    date=models.DateField()
    #list resurant names on admin page
    def __str__(self):
        return self.restaurant_name

class DoctorVisit(models.Model):
    doctor_name=models.CharField(max_length=20)
    date=models.DateField()
    #list doctor names on admin page
    def __str__(self):
        return self.doctor_name

class Symptom(models.Model):
    body_temperature=models.FloatField()
    cough_severity_index=((0,'Never'),(1,'Almost never'),(2,'Sometimes'),(3,'Almost always'),(4,'Always'))
    cough_severity=models.SmallIntegerField(choices=cough_severity_index)
    date=models.DateField()

class MedicineHistory(models.Model):
    medicine_name=models.CharField(max_length=100)
    start_date=models.DateField()
    lasting_day=models.IntegerField(default=0)
    #list medicine names on admin page
    def __str__(self):
        return self.medicine_name

class SurroundingSituation(models.Model):
    positive_people_name=models.CharField(max_length=20)
    last_meet_date=models.DateField()
    #list the name of positive people on admin page
    def __str__(self):
        return self.positive_people_name

class Trip(models.Model):
    location=models.CharField(max_length=100)
    departure_date=models.DateField()
    lasting_day=models.IntegerField(default=0)
    #list the location on admin page
    def __str__(self):
        return self.location

class Fitbit(models.Model):
    steps=models.IntegerField()
    calories=models.IntegerField()
    floors=models.IntegerField()
    distance=models.FloatField()
    weight=models.IntegerField()
    date=models.DateField()

class Apple(models.Model):
    steps=models.IntegerField()
    distance=models.FloatField()
    floors=models.IntegerField()
    calories=models.IntegerField()
    heart_rate=models.IntegerField()
    exercise_minutes=models.IntegerField()
    date=models.DateField()
    #list date on admin page
    def __str__(self):
        return self.date

class State(models.Model):
    select_state = models.CharField(max_length=30, choices=(
        ('AL','Alabama'),
        ('AK','Alaska'),
        ('AZ','Arizona'),
        ('AR','Arkansas'),
        ('CA','California'),
        ('CO','Colorado'),
        ('CT','Connecticut'),
        ('DE','Delaware'),
        ('DC','District of Columbia'),
        ('FL','Florida'),
        ('GA','Georgia'),
        ('HI','Hawaii'),
        ('ID','Idaho'),
        ('IL','Illinios'),
        ('IN','Indiana'),
        ('IA','Iowa'),
        ('KS','Kansas'),
        ('KY','Kentucky'),
        ('LA','Louisiana'),
        ('ME','Maine'),
        ('MD','Maryland'),
        ('MA','Massachusetts'),
        ('MI','Michigan'),
        ('MN','Minnesota'),
        ('MS','Mississippi'),
        ('MO','Missouri'),
        ('MT','Montana'),
        ('NE','Nebraska'),
        ('NV','Nevada'),
        ('NH','New Hampshire'),
        ('NJ','New Jersey'),
        ('NM','New Mexico'),
        ('NY','New York'),
        ('NC','North Carolina'),
        ('ND','North Dakota'),
        ('OH','Ohio'),
        ('OK','Oklahoma'),
        ('OR','Oregon'),
        ('PA','Pennsylvania'),
        ('RI','Rhode Island'),
        ('SC','South Carolina'),
        ('SD','South Dakota'),
        ('TN','Tennessee'),
        ('TX','Texas'),
        ('UT','Utah'),
        ('VT','Vermont'),
        ('VA','Virginia'),
        ('WA','Washington'),
        ('WV','West Virginia'),
        ('WI','Wisconsin'),
        ('WY','Wyoming'),
    ))


class localData(models.Model):
    population = models.IntegerField()
    cases = models.IntegerField()
    death = models.IntegerField()

    def __str__(self):
        return self.cases
