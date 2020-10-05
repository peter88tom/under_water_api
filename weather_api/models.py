from django.db import models

# Create your models here.


class Period(models.Model):
	period_name = models.CharField(max_length=250, null=True, blank=True)
	def __str__(self):
		return self.period_name


class WeatherRecord(models.Model):
	city   =  models.CharField(max_length=250, null=True, blank=True)
	period = models.ForeignKey(Period,null=True, blank=True, on_delete=models.CASCADE,related_name='period')
	min_temp    = models.CharField(max_length=250, null=True, blank=True)
	max_temp    = models.CharField(max_length=250, null=True, blank=True)
	average_temp= models.CharField(max_length=250, null=True, blank=True)
	median_temp = models.CharField(max_length=250, null=True, blank=True)

	min_humidity    = models.CharField(max_length=250, null=True, blank=True)
	max_humidity    =  models.CharField(max_length=250, null=True, blank=True)
	average_humidity= models.CharField(max_length=250, null=True, blank=True)
	median_humidity = models.CharField(max_length=250, null=True, blank=True)

	def __str__(self):
		return self.city+'('+period+')'


