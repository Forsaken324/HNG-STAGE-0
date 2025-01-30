from django.shortcuts import render
from datetime import datetime, timezone

# Create your views here.

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.decorators import api_view

@api_view(['GET'])
def home(request, *args, **kwargs) -> Response:
    now = datetime.now(timezone.utc)
    current_date = now.strftime('%Y-%m-%dT%H:%M:%SZ')


    data = {
        "email" : "davidnduonofit47@gmail.com",
        "current_datetime" : current_date,
        "github_url" : 'https://github.com/Forsaken324/HNG-STAGE-0.git'
    }

    return Response(data, status=HTTP_200_OK)