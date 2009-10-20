from django.db import models

class AccessCard(models.Model):
    pin = models.CharField(max_length=14)
    serial_no = models.CharField(max_length=12, unique=True)

    def __unicode__(self):
	return u"%s, %s" % (self.serial_no, self.pin)

    class Meta:
	verbose_name = "Access Card"
