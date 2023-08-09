from django.shortcuts import render
from django.http import JsonResponse
import json
from products.models import Product

from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.serializers import ProductSerializer


@api_view(['GET'])
def api_home(request, *args, **kwargs):
    """Django REST Framework API Home"""
    data = {}
    instance = Product.objects.all().order_by("?").first()
    if instance is not None:
        data = ProductSerializer(instance).data
    return Response(data)
