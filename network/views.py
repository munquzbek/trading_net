from rest_framework import viewsets

from network.filters import NetworkFilter
from network.models import Product, Network
from network.serializers import ProductSerializer, NetworkSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class NetworkViewSet(viewsets.ModelViewSet):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
    filterset_class = NetworkFilter

