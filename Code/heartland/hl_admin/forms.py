from django import forms

class CreateUserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    type = forms.ChoiceField((('Registrar', 'Registrar'), ('Judge', 'Judge')))
