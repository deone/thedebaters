from django import forms

class PersonForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    home_phone = forms.CharField(max_length=20)
    office_phone = forms.CharField(max_length=20)
    mobile_phone = forms. CharField(max_length=20)
    email = forms.EmailField()
    address = forms.CharField(widget=forms.Textarea)

    date_of_birth = forms.DateField()
    state_of_origin = forms.CharField(max_length=20)
    marital_status = forms.CharField(max_length=20)
    occupation = forms.CharField(max_length=50)
    hobbies = forms.CharField(widget=forms.Textarea)

    passport_photo = forms.ImageField()
    full_photo = forms.ImageField()
