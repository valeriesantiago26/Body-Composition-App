from django.db import models
from django_utils import choices

# Person model with name, gender and date of birth.
class Person(models.Model):
	
	class Gender(choices.Choices):
			Male = choices.Choice('m')
			Female = choices.Choice('f')

	firstName = models.CharField(max_length=100, default="")
	lastName = models.CharField(max_length=100, default="")
	gender = models.CharField(max_length=1, choices=Gender.choices)
	DOB = models.DateField()

	def Name(self):
		return self.firstName + ' ' + self.lastName
	

# Measurements
class Measurements(models.Model):
	person = models.ForeignKey(
        'Person',
        on_delete=models.CASCADE,
        )

	# physical
	weight_kg = models.FloatField()
	height_meters = models.FloatField()

	#skinfold
	chest = models.FloatField(null=True)
	axilla = models.FloatField(null=True)
	triceps = models.FloatField(null=True)
	subscapular = models.FloatField(null=True)
	abdomen = models.FloatField(null=True)
	suprailiac = models.FloatField(null=True)
	thigh = models.FloatField(null=True)

	results = models.FloatField()

	#def bmi(self):
    #    return self.weight_in_kg / self.height_in_meters ** 2