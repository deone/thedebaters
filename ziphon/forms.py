from datetime import date

from django import forms
from django.conf import settings

from thedebaters.ziphon.models import Person

class DateOfBirthField(forms.Field):

    def clean(self, value):
	if not value:
	    raise forms.ValidationError("Please enter your date of birth")

	try:
	    r_date = value.split("-")

	    this_year = date.today().year
	    if int(r_date[2]) < this_year-settings.PARTICIPANT_AGE_LIMIT or int(r_date[2]) > this_year:
		raise forms.ValidationError("You are too old to participate")

	    date_of_birth = date(int(r_date[2]), int(r_date[1]), int(r_date[0]))

	    return date_of_birth
	except Exception, e:	
	    raise forms.ValidationError("Your date of birth is wrong or you're too old to participate")

class PersonForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
	super(PersonForm, self).__init__(*args, **kwargs)
	self.fields['date_of_birth'] = DateOfBirthField(help_text="Format: DD-MM-YYYY")
    
    class Meta:
	model = Person

    def save(self):
	first_name = self.cleaned_data["first_name"]
	last_name = self.cleaned_data["last_name"]
	sex = self.cleaned_data["sex"]
	home_phone = self.cleaned_data["home_phone"]
	office_phone = self.cleaned_data["office_phone"]
	mobile_phone = self.cleaned_data["mobile_phone"]
	email = self.cleaned_data["email"]
	address = self.cleaned_data["address"]
	date_of_birth = self.cleaned_data["date_of_birth"]
	state_of_origin = self.cleaned_data["state_of_origin"]
	relationship_status = self.cleaned_data["relationship_status"]
	occupation = self.cleaned_data["occupation"]
	hobbies = self.cleaned_data["hobbies"]

	new_person = Person.objects.create(first_name=first_name, \
		last_name=last_name, sex=sex, \
		home_phone=home_phone, office_phone=office_phone, \
		mobile_phone=mobile_phone, email=email, address=address, \
		date_of_birth=date_of_birth, state_of_origin=state_of_origin, \
		relationship_status=relationship_status, \
		occupation=occupation, hobbies=hobbies)
	new_person.save()

	return new_person
