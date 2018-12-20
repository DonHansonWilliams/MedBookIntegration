from django.shortcuts import render
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from members.models import MemberDetails
from members.models import CoverBenefits


@api_view(http_method_names=['GET', ])
@renderer_classes((JSONRenderer,))
def fetchmember(request, memno):
    member_number = memno.replace("-", "/", 4)
    details = dict()
    try:
        member_details = MemberDetails.objects.get(member_no=member_number)
        details = {
            'scheme_code': member_details.scheme_code,
            'family_no': member_details.family_no,
            'member_no': member_details.member_no,
            'member_name': member_details.member_name,
            'mobile_no': member_details.mobile_no,
            'member_status': member_details.member_status,
            'gender': member_details.gender,
            'dob': member_details.dob,
            'start_date': member_details.start_date,
            'end_date': member_details.end_date,
            'anniv': member_details.anniv
        }
    except MemberDetails.DoesNotExist:

        return Response(details)

    return Response(details)


@api_view(http_method_names=['GET', ])
@renderer_classes((JSONRenderer,))
def fetchcoverbenefits(request, memno):
    member_number = memno.replace("-", "/", 4)
    coverbenefit = CoverBenefits.objects.filter(member_no=member_number)
    member_benefit = []
    try:
        memberBenefit = CoverBenefits.objects.filter(member_no=member_number)

        for i in memberBenefit:
            benefits = {
                'scheme_code': i.scheme_code,
                'family_no': i.family_no,
                'member_no': i.member_no,
                'benefit': i.benefit,
                'benefit_code': i.benefit_code,
                'benefit_limit': i.benefit_limit,
                'waiting_period': i.waiting_period,
                'anniv': i.anniv,
                'reserves': i.reserves,
                'expenditure': i.expenditure,
                'balance': i.balance,

            }
            member_benefit.append(benefits)
    except CoverBenefits.DoesNotExist:
        return Response(member_benefit)

    return Response(member_benefit)


@api_view(http_method_names=['GET', ])
@renderer_classes((JSONRenderer,))
def postmembers(request):
    member = MemberDetails.objects.all()
    members = []
    for i in member:
        mem = {'scheme_code': i.scheme_code,
               'family_no': i.family_no,
               'member_no': i.member_no,
               'member_name': i.member_name,
               'mobile_no': i.mobile_no,
               'gender': i.gender,
               'dob': i.dob,
               'member_status': i.member_status,
               'start_date': i.start_date,
               'end_date': i.end_date,
               'anniv': i.anniv,
               }
        members.append(mem)

    return Response(members)
