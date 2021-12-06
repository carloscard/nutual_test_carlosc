from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context
from django.template import loader
from nutual_app.inquiries import DbInquiries
from nutual_code_challenge.business.data_views import DataViews
import requests


class MainView:

    def __init__(self):
        self.inquiries_obj = DbInquiries()
        self.data_views_obj = DataViews()

    def display_api_data(self, request):

        # Get flats Data from avm and avg apis
        response_avm = requests.get('http://127.0.0.1:8000/api-avm/avm-api/').json()
        response_avg = requests.get('http://127.0.0.1:8000/api-avg/avg-m2-api/').json()

        # Insert data into DB
        self.inquiries_obj.insert_data(response_avm)

        # Get flats Data from DB
        all_flats = self.inquiries_obj.get_data_nutal_bd()

        # Give dictionary format to use data easily
        flats_format = self.data_views_obj.data_flats(all_flats)

        ciudades = response_avg
        # Display the template and passing data
        doc_externo = loader.get_template('index.html')

        documento = doc_externo.render({"flats_format": flats_format, "ciudades":ciudades})
        return HttpResponse(documento)
