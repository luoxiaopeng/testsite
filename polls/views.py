from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import permissions
from adrf.views import APIView


class TestApiView(APIView):
    # permission_classes = [permissions.AllowAny]
    authentication_classes = []

    def get(self, request, *args, **kwargs):
        return Response({"message": "This is an async class based view."})
