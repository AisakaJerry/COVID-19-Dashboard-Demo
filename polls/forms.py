from django import forms
from .models import Takeout,DoctorVisit,Symptom,MedicineHistory,SurroundingSituation,Trip, State
import datetime
today=datetime.date.today()
this_month=today.month
this_year=today.year

#it tells django which model to create the form from
class TopicFormTakeout(forms.ModelForm):
    date=forms.DateField(widget=forms.SelectDateWidget(years=range(2021,2025)))
    class Meta:
        model=Takeout
        fields=['restaurant_name','dishes','date']

class TopicFormDoctorVisit(forms.ModelForm):
    date=forms.DateField(widget=forms.SelectDateWidget(years=range(2021,2025)))
    class Meta:
        model=DoctorVisit
        fields=['doctor_name','date']

class TopicFormSymptom(forms.ModelForm):
    date=forms.DateField(widget=forms.SelectDateWidget(years=range(2021,2025)))
    class Meta:
        model=Symptom
        fields=['body_temperature','cough_severity','date']

class TopicFormMedicineHistory(forms.ModelForm):
    start_date=forms.DateField(widget=forms.SelectDateWidget(years=range(2021,2025)))
    class Meta:
        model=MedicineHistory
        fields=['medicine_name','start_date','lasting_day']

class TopicFormSurroundingSituation(forms.ModelForm):
    last_meet_date = forms.DateField(widget=forms.SelectDateWidget(years=range(2021,2025)))
    class Meta:
        model=SurroundingSituation
        fields=['positive_people_name','last_meet_date']

class TopicFormTrip(forms.ModelForm):
    departure_date=forms.DateField(widget=forms.SelectDateWidget(years=range(2021,2025)))
    class Meta:
        model=Trip
        fields=['location','departure_date','lasting_day']

class SelectStateForm(forms.Form):
    SELVALUE = State.SELVALUE
    sel_value = forms.CharField(max_length=10, widget=forms.widgets.Select(choices=SELVALUE))
