from django import forms
from .models import Names


class NameForm(forms.ModelForm):
    class Meta:
        model = Names
        fields = ['first_name', 'last_name']
