from django.db import IntegrityError
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

# Create your views here.
from preauth.models import Preauth


@api_view(http_method_names=['POST', ])
@renderer_classes((JSONRenderer,))
def savepreauth(request):
    try:
        pre_auth = Preauth(
            member_no=request.data['member_no'],
            date_requested=request.data['date_requested'],
            diagnosis=request.data['diagnosis'],
            ben_code=request.data['ben_code'],
            prov_code=request.data['prov_code'],
            requested_amt=request.data['requested_amount'],
            deducted_amt=request.data['deducted_amount'],
            deduction_reason=request.data['deduction_reason'],
            approved_amount=request.data['approved_amount'],
            request_notes=request.data['request_notes'],
            requested_by=request.data['requested_by'],
        )
        pre_auth.save()
        msg = "Save of Pre-auth success"
    except IntegrityError:
        msg = "Save of Pre-auth failed"

    return Response(msg)
