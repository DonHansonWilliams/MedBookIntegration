from django.db import IntegrityError
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from django.shortcuts import render

# Create your views here.
from claims.models import Claim, MedbookClaims, ClaimStatus, Reimbursements, ClaimsExperience


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


@api_view(http_method_names=['POST', ])
@renderer_classes((JSONRenderer,))
def storeClaim(request):
    if _checkduplicate(request):
        return Response("Claim Exists")

    _claim = MedbookClaims(

        smart_provider=request.data['provCode'],
        smart_trans_date=request.data['invoiceDate'],
        smart_service=request.data['service'],
        smart_benefit=request.data['benCode'],
        smart_bill_amount=request.data['InvoicedAmt'],
        uploaded=0,
        vetted=1,
        anniv=request.data['anniv'],
        smart_member_no=request.data['memberNo'],
        smart_inv_no=request.data['invoiceNo'],
        pre_auth_no=request.data['pre_auth_no'],
        fund=request.data['fund'],
        family_no=request.data['family_no'],
        corp_id=request.data['corp_id'],
        smart_bill_id=request.data['invoiceNo'],
        claim_source="MedBook",
    )
    _claim.save()
    msg = "Success"

    return Response(msg)


def _checkduplicate(claim):
    try:
        exists = MedbookClaims.objects.filter(
            smart_provider=claim.data['provCode'],
            smart_inv_no=claim.data['invoiceNo'],
            smart_service=claim.data['service']
        ).count()
        if exists > 0:
            resp = True
        else:
            resp = False
    except MedbookClaims.DoesNotExist:
        resp = False
    return resp


@api_view(http_method_names=['POST', ])
@renderer_classes((JSONRenderer,))
def fetchclaimstatus(request):
    status_details = dict()
    try:
        claim_details = ClaimStatus.objects.get(
            bill_id=request.data['bill_id']
        )
        status_details = {
            'invoice_no': claim_details.invoice_no,
            'bill_id': claim_details.bill_id,
            'service': claim_details.service,
            'member_no': claim_details.member_no,
            'anniv': claim_details.anniv,
            'hospital': claim_details.hospital,
            'provider_code': claim_details.provider_code,
            'vet_status': claim_details.vet_status,
            'date_entered': claim_details.date_entered,
            'invoiced_amount': claim_details.invoiced_amount,
            'deduction_amount': claim_details.deduction_amount,
            'amount_payable': claim_details.amount_payable
        }
    except ClaimStatus.DoesNotExist:

        return Response(status_details)

    return Response(status_details)


@api_view(http_method_names=['GET', ])
@renderer_classes((JSONRenderer,))
def fetchreimb(request, memno):
    member_number = memno.replace("-", "/", 4)
    details = []
    try:
        memberReimb = Reimbursements.objects.filter(member_no=member_number)

        for i in memberReimb:
            reimb = {
                'invoice_no': i.invoice_no,
                'service': i.service,
                'member_no': i.member_no,
                'anniv': i.anniv,
                'hospital': i.hospital,
                'provider_code': i.provider_code,
                'date_entered': i.date_entered,
                'invoiced_amount': i.invoiced_amount,
                'deduction_amount': i.deduction_amount,
                'amount_payable': i.amount_payable
            }
            details.append(reimb)
    except Reimbursements.DoesNotExist:

        return Response(details)

    return Response(details)


@api_view(http_method_names=['GET', ])
@renderer_classes((JSONRenderer,))
def fetchreimbs(request):
    details = []
    try:
        fetchreimbs = Reimbursements.objects.all()

        for i in fetchreimbs:
            reimb = {
                'invoice_no': i.invoice_no,
                'service': i.service,
                'member_no': i.member_no,
                'anniv': i.anniv,
                'hospital': i.hospital,
                'provider_code': i.provider_code,
                'date_entered': i.date_entered,
                'invoiced_amount': i.invoiced_amount,
                'deduction_amount': i.deduction_amount,
                'amount_payable': i.amount_payable
            }
            details.append(reimb)
    except Reimbursements.DoesNotExist:

        return Response(details)

    return Response(details)


@api_view(http_method_names=['GET', ])
@renderer_classes((JSONRenderer,))
def claims_exp(request):
    details = []
    try:
        claims_exp = ClaimsExperience.objects.all()

        for i in claims_exp:
            experience = {
                'corporate': i.corporate,
                'principal_name': i.principal_name,
                'member_name': i.member_name,
                'family_no': i.family_no,
                'member_no': i.member_no,
                'relation': i.relation,
                'claim_no': i.claim_no,
                'anniv': i.anniv,
                'provider': i.provider,
                'invoice_no': i.invoice_no,
                'service': i.service,
                'invoice_date': i.invoice_date,
                'benefit': i.date_received,
                'date_received': i.service,
                'date_entered': i.date_entered,
                'invoiced_amount': i.invoiced_amount,
                'amount_payable': i.amount_payable,

            }
            details.append(experience)
    except ClaimsExperience.DoesNotExist:

        return Response(details)

    return Response(details)


@api_view(http_method_names=['GET', ])
@renderer_classes((JSONRenderer,))
def fetch_fam_exp(request, family, year):
    family_number = family.replace("-", "/")
    details = []
    try:
        famExperience = ClaimsExperience.objects.filter(family_no=family_number, anniv=year)

        for i in famExperience:
            experience = {
                'corporate': i.corporate,
                'principal_name': i.principal_name,
                'member_name': i.member_name,
                'family_no': i.family_no,
                'member_no': i.member_no,
                'relation': i.relation,
                'claim_no': i.claim_no,
                'anniv': i.anniv,
                'provider': i.provider,
                'invoice_no': i.invoice_no,
                'service': i.service,
                'invoice_date': i.invoice_date,
                'benefit': i.date_received,
                'date_received': i.service,
                'date_entered': i.date_entered,
                'invoiced_amount': i.invoiced_amount,
                'amount_payable': i.amount_payable,
            }
            details.append(experience)
    except ClaimsExperience.DoesNotExist:

        return Response(details)

    return Response(details)


@api_view(http_method_names=['GET', ])
@renderer_classes((JSONRenderer,))
def fetch_member_statement(request, member, year):
    member_number = member.replace("-", "/")
    details = []
    try:
        memberStatemement = ClaimsExperience.objects.filter(member_no=member_number, anniv=year)

        for i in memberStatemement:
            experience = {
                'corporate': i.corporate,
                'principal_name': i.principal_name,
                'member_name': i.member_name,
                'family_no': i.family_no,
                'member_no': i.member_no,
                'relation': i.relation,
                'claim_no': i.claim_no,
                'anniv': i.anniv,
                'provider': i.provider,
                'invoice_no': i.invoice_no,
                'service': i.service,
                'invoice_date': i.invoice_date,
                'benefit': i.date_received,
                'date_received': i.service,
                'date_entered': i.date_entered,
                'invoiced_amount': i.invoiced_amount,
                'amount_payable': i.amount_payable,
            }
            details.append(experience)
    except ClaimsExperience.DoesNotExist:

        return Response(details)

    return Response(details)
