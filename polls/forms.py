from django import forms
from .models import Takeout
from .models import State

#it tells django which model to create the form from
class TopicForm(forms.ModelForm):
    class Meta:
        model=Takeout
        fields=['restaurant_name','dishes','date']

class SelectStateForm(forms.Form):
    SELVALUE = State.SELVALUE
    sel_value = forms.CharField(max_length=10, widget=forms.widgets.Select(choices=SELVALUE))