from django.shortcuts import render,redirect
from django.http import request, HttpResponseRedirect,HttpResponse,JsonResponse
from django.core import serializers
from .models import *

def get_weather(request):
	if request.method == 'POST':
		# ToDo
		# posted data, fetch the weather from any api
		pass
	else:
		periods = Period.objects.all()
		return render(request, 'weather_api/index.html',{
			'periods':periods,
			})