from django.urls import path
from .views import *

urlpatterns = [
    path('weather/', WeatherData.as_view()),
    path('news/', NewsData.as_view())
]