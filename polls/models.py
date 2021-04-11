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
    def __str__(self):
        return self.date

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

class State(models.Model):
    SELVALUE = (
        ('Alabama', 'AL'),
        ('Alaska', 'AK'),
        ('Arizona', 'AZ'),
        ('Arkansas', 'AR'),
        ('California', 'CA'),
        ('Colorado', 'CO'),
        ('Connecticut', 'CT'),
        ('Delaware', 'DE'),
        ('District of Columbia', 'DC'),
        ('Florida', 'FL'),
        ('Georgia', 'GA'),
        ('Hawaii', 'HI'),
        ('Idaho', 'ID'),
        ('Illinios', 'IL'),
        ('Indiana', 'IN'),
        ('Iowa', 'IA'),
        ('Kansas', 'KS'),
        ('Kentucky', 'KY'),
        ('Louisiana', 'LA'),
        ('Maine', 'ME'),
        ('Maryland', 'MD'),
        ('Massachusetts', 'MA'),
        ('Michigan', 'MI'),
        ('Minnesota', 'MN'),
        ('Mississippi', 'MS'),
        ('Missouri', 'MO'),
        ('Montana', 'MT'),
        ('Nebraska', 'NE'),
        ('Nevada', 'NV'),
        ('New Hampshire', 'NH'),
        ('New Jersey', 'NJ'),
        ('New Mexico', 'NM'),
        ('New York', 'NY'),
        ('North Carolina', 'NC'),
        ('North Dakota', 'ND'),
        ('Ohio', 'OH'),
        ('Oklahoma', 'OK'),
        ('Oregon', 'OR'),
        ('Pennsylvania', 'PA'),
        ('Rhode Island', 'RI'),
        ('South Carolina', 'SC'),
        ('South Dakota', 'SD'),
        ('Tennessee', 'TN'),
        ('Texas', 'TX'),
        ('Utah', 'UT'),
        ('Vermont', 'VT'),
        ('Virginia', 'VA'),
        ('Washington', 'WA'),
        ('West Virginia', 'WV'),
        ('Wisconsin', 'WI'),
        ('Wyoming', 'WY'),
    )
    select_value = models.CharField(max_length=30, choices=SELVALUE)
    # list the selected state on admin page
    def __str__(self):
        return self.select_value
