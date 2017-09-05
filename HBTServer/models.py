from django.db import models
from location_field.models.plain import PlainLocationField
from django_pgjsonb import JSONField

# Create your models here.
class HBT(models.Model):
	class Head(models.Model):
		HBT_ID = models.IntegerField(null=True)
		Time = models.DateTimeField(auto_now = True)
		Location = PlainLocationField(based_fields=['city'], zoom=7)

	class Body(models.Model):
		Type = models.CharField(null=True, max_length=20)
		#DataSequence = models.IntegerField(null=True)
		DataSequence = JSONField(null=True)

	class Tail(models.Model):
	    Result = models.TextField(null=True)
	    Accuracy = models.FloatField(null=True)

	class Bodydata(models.Model):
	    Heart = models.IntegerField(null=True)
	    Skin = models.IntegerField(null=True)
	    Myo = models.IntegerField(null=True)
	    Mic = models.FloatField(null=True)