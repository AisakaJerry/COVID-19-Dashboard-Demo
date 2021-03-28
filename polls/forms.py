from django import forms
from .models import Takeout

#it tells django which model to create the form from
class TopicForm(forms.ModelForm):
    class Meta:
        model=Takeout
        fields=['restaurant_name','dishes','date']