from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from users.models import User


@api_view(http_method_names=['GET', ])
@renderer_classes((JSONRenderer,))
def fetch_users(request):

    all_users = User.objects.all()
    users = []
    for i in all_users:
        user = {'username': i.user_name,
                'password': i.user_pass}
        users.append(user)

    return Response(users)
