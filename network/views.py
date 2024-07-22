from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied

from network.filters import NetworkFilter
from network.models import Product, Network
from network.serializers import ProductSerializer, NetworkSerializer
from users.permissions import IsActiveEmployee


class ProductViewSet(viewsets.ModelViewSet):
    """VieSet for Product model"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActiveEmployee]


class NetworkViewSet(viewsets.ModelViewSet):
    """VieSet for Network model"""
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
    filterset_class = NetworkFilter
    permission_classes = [IsActiveEmployee]

    # filtering objects for the current user with connected networks
    def get_queryset(self):
        return Network.objects.filter(id=self.request.user.network.id)

    # additional validator check that the requested object belongs to the current user's network
    # get_queryset already filtering it, but this is for more reliability
    def get_object(self):
        obj = super().get_object()
        if obj.id != self.request.user.network.id:
            raise PermissionDenied("You do not have permission to access this network.")
        return obj

