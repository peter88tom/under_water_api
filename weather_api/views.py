from django.shortcuts import render,redirect
from django.http import request, HttpResponseRedirect,HttpResponse,JsonResponse
from django.core import serializers

def get_weather(request):
	if request.method == 'POST':
		pass
	else:
		return render(request, 'weather_api/index.html',)