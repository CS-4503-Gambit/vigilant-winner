from django import forms
from core.models import *

class RegistrationForm(forms.Form):
    team_name = forms.CharField()
    entry_name = forms.CharField()
    category = forms.ModelChoiceField(queryset=Category.objects.all().order_by('name'), to_field_name='name')
