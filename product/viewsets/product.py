from rest_framework.viewsets import ModelViewSet

from product.models.product import Product
from product.serializers.product import ProductSerializer


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
