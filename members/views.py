from django.shortcuts import render
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from members.models import Member
from members.models import CoverBenefits

@api_view(http_method_names=['GET', ])
@renderer_classes((JSONRenderer,))
def fetchmember(request,memno):
    member_number = memno.replace("-","/",4)
    member_details = Member.objects.get(member_no=member_number)
    details = {'scheme_code': member_details.scheme_code,
            'member_no': member_details.member_no,
            'member_name': member_details.member_names,
            'member_status': member_details.member_status,
            'start_date': member_details.start_date,
            'end_date': member_details.end_date,
            'mobile_no': member_details.mobile_no,
            'anniv': member_details.anniv
            }
    return Response(details)

@api_view(http_method_names=['GET', ])
@renderer_classes((JSONRenderer,))
def fetchcoverbenefits(request,memno):
    member_number = memno.replace("-", "/", 4)
    coverbenefit = CoverBenefits.objects.filter(member_no=member_number)
    member_benefit = []
    for i in coverbenefit:
        benefitdetails = {'benefits': i.benefits,
                'scheme_code': i.scheme_code,
                          'family_no': i.family_no,
                          'member_no': i.member_no,
                          'benefit_limit': i.benefit_limit,
                          'claims': i.claims,
                          'reserve_amount': i.reserve_amount,
                          'expense': i.expense,
                          'benefit_status': i.benefit_status,
                          'balance': i.balance,
                          'waiting_period': i.waiting_period,
                          'ben_code': i.ben_code
                          }
        member_benefit.append(benefitdetails)

    return Response(member_benefit)