from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #lookup_field = 'pk'

class ProductCreateAPIView(generics.CreateAPIView):
    """A Django view to create a product"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        """Override the default create behavior of the Django REST Framework"""
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if not content:
            content = title
        serializer.save(content=content)