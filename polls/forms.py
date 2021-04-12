from django import forms
from .models import Takeout,DoctorVisit,Symptom,MedicineHistory,SurroundingSituation,Trip,Fitbit,Apple, State, localData

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
    last_meet_date=forms.DateField(widget=forms.SelectDateWidget(years=range(2021,2025)))
    class Meta:
        model=SurroundingSituation
        fields=['positive_people_name','last_meet_date']

class TopicFormTrip(forms.ModelForm):
    departure_date=forms.DateField(widget=forms.SelectDateWidget(years=range(2021,2025)))
    class Meta:
        model=Trip
        fields=['location','departure_date','lasting_day']

class TopicFormFitbit(forms.ModelForm):
    class Meta:
        model=Fitbit
        fields=['steps','calories','floors','distance','weight','date']

class TopicFormApple(forms.ModelForm):
    class Meta:
        model=Apple
        fields=['steps','distance','floors','calories','heart_rate','exercise_minutes','date']

class SelectStateForm(forms.ModelForm):
    SELVALUE = State.SELVALUE
    sel_value = forms.CharField(max_length=10, widget=forms.widgets.Select(choices=SELVALUE))

    class Meta:
        model = State
        fields = ['select_value']

class localDataForm(forms.ModelForm):
    class Meta:
        model = localData
        fields=['population', 'cases', 'death']