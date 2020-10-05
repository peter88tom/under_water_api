from django.urls import path
from weather_api import views

urlpatterns = [
    path('', views.get_weather, name='default-page')
]


