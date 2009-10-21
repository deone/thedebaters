from django import forms

class LoginForm(forms.Form):
    pin = forms.CharField(label="PIN", max_length=30, widget=forms.TextInput())
    serial_no = forms.CharField(label="Serial No.", widget=forms.TextInput())
