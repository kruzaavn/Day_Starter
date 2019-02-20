from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from Backend.settings import API_KEYS
from newsapi import NewsApiClient
import requests
import json

# Create your views here.


class WeatherData(APIView):

    def get(self, request, format=None):

        key = '?APPID={}'.format(API_KEYS['OpenWeatherAPI'])
        url = 'http://api.openweathermap.org/data/2.5/'

        if request.query_params.get('forecast'):
            query = url + 'forecast' + key
        else:
            query = url + 'weather' + key

        if request.query_params.get('id'):
            query += '&id={}'.format(request.query_params.get('id'))

            return Response(requests.get(query).json(), status=status.HTTP_200_OK)

        if request.query_params.get('city'):
            query += '&q={}'.format(request.query_params.get('city'))

            return Response(requests.get(query).json(), status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)


class NewsData(APIView):

    def get(self, request, format=None):

        call = NewsApiClient(api_key=API_KEYS['NewsAPI'])

        return Response(call.get_top_headlines(sources='the-washington-post,bbc-news,the-new-york-times', language='en'), status=status.HTTP_200_OK)
