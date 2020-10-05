from django.shortcuts import render,redirect
from django.http import request, HttpResponseRedirect,HttpResponse,JsonResponse
from django.core import serializers
from .models import *
import time

def get_weather(request):
	if request.method == 'POST':
		# ToDo
		# posted data, fetch the weather from any api
		time.sleep(5)
		pass
	else:
		periods = Period.objects.all()
		return render(request, 'weather_api/index.html',{
			'periods':periods,
			})