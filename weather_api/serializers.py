from django.db import models
from rest_framework import serializers
from weather_api.models import WeatherRecord


class WeatherSerializer(serializers.ModelSerializer):
	class Meta:
		model= WeatherRecord
		fields = ('city','period')
