from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from schemes.models import Scheme


@api_view(http_method_names=['GET', ])
@renderer_classes((JSONRenderer,))
def fetchschemes(request):

    scheme = Scheme.objects.all()
    schemes = []
    for i in scheme:
        corp = {'corp_id': i.corp_id,
                'scheme_code': i.scheme_code,
                'scheme_name': i.scheme_name}
        schemes.append(corp)

    return Response(schemes)
