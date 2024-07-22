from rest_framework import serializers

from network.models import Product, Network


class ProductSerializer(serializers.ModelSerializer):
    """Serializer for Product model"""

    class Meta:
        model = Product
        fields = '__all__'


class NetworkSerializer(serializers.ModelSerializer):
    """Serializer for Network model"""

    class Meta:
        model = Network
        fields = '__all__'

    # changing debt is prohibited
    def validate(self, data):
        if 'debt_to_supplier' in data:
            raise serializers.ValidationError({'debt_to_supplier': 'Debt cannot be updated.'})
        return data
