from django.db import models

class AccessCard(models.Model):
    pin = models.CharField(max_length=14)
    serial_no = models.CharField(max_length=12, unique=True)

    def __unicode__(self):
	return u"%s, %s" % (self.serial_no, self.pin)

    def check_serial_no(self, raw_serial_no):
	is_correct = (self.serial_no == raw_serial_no)
	return is_correct
