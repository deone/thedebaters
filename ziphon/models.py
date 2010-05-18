from django.db import models

SEX_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
)

STATE_CHOICES = (
    ("Abia", "Abia"),
    ("Abuja", "Abuja"),
    ("Adamawa", "Adamawa"),
    ("Akwa Ibom", "Akwa Ibom"),
    ("Anambra", "Anambra"),
    ("Bauchi", "Bauchi"),
    ("Bayelsa", "Bayelsa"),
    ("Benue", "Benue"),
    ("Borno", "Borno"),
    ("Cross-River", "Cross-River"),
    ("Delta", "Delta"),
    ("Ebonyi", "Ebonyi"),
    ("Edo", "Edo"),
    ("Ekiti", "Ekiti"),
    ("Enugu", "Enugu"),
    ("Gombe", "Gombe"),
    ("Imo", "Imo"),
    ("Jigawa", "Jigawa"),
    ("Kaduna", "Kaduna"),
    ("Kano", "Kano"),
    ("Katsina", "Katsina"),
    ("Kebbi", "Kebbi"),
    ("Kogi", "Kogi"),
    ("Nasarawa", "Nasarawa"),
    ("Niger", "Niger"),
    ("Ogun", "Ogun"),
    ("Ondo", "Ondo"),
    ("Osun", "Osun"),
    ("Oyo", "Oyo"),
    ("Kwara", "Kwara"),
    ("Lagos", "Lagos"),
    ("Plateau", "Plateau"),
    ("Rivers", "Rivers"),
    ("Sokoto", "Sokoto"),
    ("Taraba", "Taraba"),
    ("Yobe", "Yobe"),
    ("Zamfara", "Zamfara")
)

RELATIONSHIP_STATUS_CHOICES = (
    ("Single", "Single"),
    ("In a committed relationship", "In a committed relationship"),
    ("Married", "Married"),
    ("Separated", "Separated"),
    ("Divorced", "Divorced"),
)

class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    sex = models.CharField(max_length=6, choices=SEX_CHOICES)
    home_phone = models.CharField(max_length=20)
    office_phone = models.CharField(max_length=20)
    mobile_phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()

    date_of_birth = models.DateField()
    state_of_origin = models.CharField(max_length=20, choices=STATE_CHOICES)
    relationship_status = models.CharField(max_length=20, choices=RELATIONSHIP_STATUS_CHOICES)
    occupation = models.CharField(max_length=50)
    hobbies = models.TextField()

    def __unicode__(self):
	return "%s, %s" % (self.first_name, self.last_name)
