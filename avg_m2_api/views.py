from rest_framework.views import APIView
from rest_framework.response import Response
import json
import os
from pathlib import Path


class AvgM2Api(APIView):
    """This class is an API which returns the average of m2 from cities"""

    def __init__(self):
        self.BASE_DIR = Path(__file__).resolve().parent.parent

    def get(self, request):
        json_file = os.path.join(self.BASE_DIR, 'static/json/avg_m2.json')
        open_json = open(json_file)

        # Returns json obj as a dictionary
        avg_json = json.load(open_json)
        open_json.close()

        return Response(avg_json)