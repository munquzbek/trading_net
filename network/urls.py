from rest_framework import routers

from network.apps import NetworkConfig
from network.views import ProductViewSet, NetworkViewSet

app_name = NetworkConfig.name

router = routers.DefaultRouter()
router.register(r'product', ProductViewSet, basename='product')
router.register(r'network', NetworkViewSet, basename='network')

urlpatterns = [
] + router.urls
