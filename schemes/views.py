from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from schemes.models import Scheme, SchemeGroups


@api_view(http_method_names=['GET', ])
@renderer_classes((JSONRenderer,))
def fetchschemes(request):
    scheme = Scheme.objects.all()
    schemes = []
    for i in scheme:
        corp = {'corp_id': i.corp_id,
                'scheme_code': i.scheme_code,
                'scheme_name': i.scheme_name,
                'start_date': i.start_date,
                'end_date': i.end_date,
                'renewal_date': i.renewal_date,
                'anniv': i.anniv
                }
        schemes.append(corp)

    return Response(schemes)


@api_view(http_method_names=['GET', ])
@renderer_classes((JSONRenderer,))
def fetch_scheme_groups(request):
    details = []
    try:
        fetch_groups = SchemeGroups.objects.all()

        for i in fetch_groups:
            scheme_group = {
                'category': i.category,
                'benefit': i.benefit,
                'ben_code': i.ben_code,
                'ben_limit': i.ben_limit,
                'anniv': i.anniv,
                'ben_share': i.ben_share,
                'corp_id': i.corp_id
            }
            details.append(scheme_group)
    except SchemeGroups.DoesNotExist:

        return Response(details)

    return Response(details)


@api_view(http_method_names=['GET', ])
@renderer_classes((JSONRenderer,))
def schemeGroups(request, scheme_id):
    details = []
    try:
        scheme_group = SchemeGroups.objects.filter(corp_id=scheme_id)

        for i in scheme_group:
            group = {
                'category': i.category,
                'benefit': i.benefit,
                'ben_code': i.ben_code,
                'ben_limit': i.ben_limit,
                'anniv': i.anniv,
                'ben_share': i.ben_share,
                'corp_id': i.corp_id
            }
            details.append(group)
    except SchemeGroups.DoesNotExist:

        return Response(details)

    return Response(details)
