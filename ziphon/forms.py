from django import forms
from thedebaters.ziphon.models import Person

class PersonForm(forms.ModelForm):
    class Meta:
	model = Person
