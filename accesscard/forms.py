from django import forms
from django.contrib.auth import authenticate

class AccessForm(forms.Form):
    pin = forms.CharField(label="PIN", max_length=30, widget=forms.TextInput())
    serial_no = forms.CharField(label="Serial No.", max_length=30, widget=forms.TextInput())

    def clean(self):
	if self._errors:
	    return
	pin = self.cleaned_data["pin"]
	serial_no = self.cleaned_data["serial_no"]

	card = authenticate(pin=pin, serial_no=serial_no)
	return self.cleaned_data
