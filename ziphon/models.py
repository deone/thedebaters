from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    home_phone = models.CharField(max_length=20)
    office_phone = models.CharField(max_length=20)
    mobile_phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()

    date_of_birth = models.DateField()
    state_of_origin = models.CharField(max_length=20)
    marital_status = models.CharField(max_length=20)
    occupation = models.CharField(max_length=50)
    hobbies = models.TextField()

    passport_photo = models.ImageField(upload_to="photo/passport")
    full_photo = models.ImageField(upload_to="photo/full")

    def __unicode__(self):
	return "%s, %s" % (self.first_name, self.last_name)
    
class NextOfKin(models.Model):
    pass
