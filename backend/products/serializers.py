from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Product


class ProductSerializer(ModelSerializer):
    my_discount = SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount'
        ]

    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj.id, Product):
            return None
        return obj.price * 0.85
