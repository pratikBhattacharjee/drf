from rest_framework.serializers import ModelSerializers

from .models import Product


class ProductSerializer(ModelSerializers):
    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'content',
            'price',
            'sale_price'
        ]
