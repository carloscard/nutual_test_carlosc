from rest_framework.views import APIView
from rest_framework.response import Response
from avm_api import serializer
import json
import os
from pathlib import Path


class AvmApiView(APIView):
    """This class is an API which returns AVM data"""
    serializer_class = serializer.AvmApiSerializer

    def __init__(self):
        self.BASE_DIR = Path(__file__).resolve().parent.parent

    def get(self, request, format=None):
        """retrun json """

        json_file = os.path.join(self.BASE_DIR, 'static/json/avm.json')
        open_json = open(json_file)

        # Returns json obj as a dictionary
        avm_json = json.load(open_json)
        open_json.close()

        return Response(avm_json)

