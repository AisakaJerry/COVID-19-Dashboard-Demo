from django.db import models

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