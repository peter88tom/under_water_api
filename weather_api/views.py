from django.shortcuts import render,redirect
from django.http import request, HttpResponseRedirect,HttpResponse,JsonResponse
from django.core import serializers
from .models import *
import time
from admin.settings import WEATHER_API_KEY1
import requests
import numpy as np


def get_weather(request):
	if request.method == 'POST':
		city = request.POST['city']

		# posted data, fetch the weather from any api
		# This Api can only return current weather of a given price
		# Its possible to get the weather by 4,5,16 and 30 days but require purchase
		resp=requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid='+WEATHER_API_KEY1).json()
		

		# Calculate average and medium templature using max and min temp, will be using Numpy as it has this functions
		np_average = np.arange(resp['main']['temp_min'],resp['main']['temp_max'])
		
		# mean
		temp_average = np.average(np_average)



		# median
		temp_median = np.median(np_average)



		query_result = {
			'city':city,
			'min_temp':resp['main']['temp_min'],
			'max_temp':resp['main']['temp_max'],
			'average_temp' :temp_average,
			'median_temp' :temp_median,
			'humidity':resp['main']['humidity'],
			'icon':resp['weather'][0]['icon'],
			'description':resp['weather'][0]['description'],
			}
		
		return JsonResponse(query_result)
	else:
		periods = Period.objects.all()
		return render(request, 'weather_api/index.html',{
			'periods':periods,
			})