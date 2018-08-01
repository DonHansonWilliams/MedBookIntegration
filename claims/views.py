from django.db import IntegrityError
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from django.shortcuts import render

# Create your views here.
from claims.models import Claim


@api_view(http_method_names=['POST', ])
@renderer_classes((JSONRenderer,))
def saveclaim(request):
    if _checkduplicate(request):
        return Response("Claim Exists")

    try:
        claim = Claim(
            member_no=request.data['memberNo'],
            prov_code=request.data['provCode'],
            invoice_no=request.data['invoiceNo'],
            service=request.data['service'],
            invoice_date=request.data['invoiceDate'],
            ben_code=request.data['benCode'],
            invoiced_amt=request.data['InvoicedAmt']
        )
        claim.save()
        msg = "Success"
    except IntegrityError:
        msg = "Failed!"

    return Response(msg)


def _checkduplicate(claim):
    try:
        exists = Claim.objects.filter(
            prov_code=claim.data['provCode'],
            invoice_no=claim.data['invoiceNo'],
            service=claim.data['service'],
        ).count()
        if exists > 0:
            resp = True
        else:
            resp = False
    except Claim.DoesNotExist:
        resp = False
    return resp
