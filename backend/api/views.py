from django.shortcuts import render
from django.http import JsonResponse
import json
from products.models import Product

from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.serializers import ProductSerializer


@api_view(['POST'])
def api_home(request, *args, **kwargs):
    """Django REST Framework API Home"""
    serialized_data = ProductSerializer(data=request.data)
    if serialized_data.is_valid(raise_exception=True):
        print(serialized_data.data)
        return Response(serialized_data.data)
