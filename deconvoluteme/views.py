from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import json
from time import sleep
from spectranalyzer import LaurdanFitter

class DeconvoluteMe(APIView):
    #permission_classes = (IsAuthenticated,)

    def post(self, request):
        spectra = request.data#json.loads(request.data)
        content = {'message': 'Hello, World!',
                  'data': ''}
        fitter = LaurdanFitter()
        fitter.load_data_from_json(spectra)
        fitter.fit_all_columns()
        return Response(fitter.jsondata)

