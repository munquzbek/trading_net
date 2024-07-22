from rest_framework.serializers import ModelSerializer

from users.models import User


class UserSerializer(ModelSerializer):
    """Serializer for User model except CreateView"""
    class Meta:
        model = User
        fields = '__all__'


class UserCreateSerializer(ModelSerializer):
    """Serializer for creating View of User, can use only email and password"""
    class Meta:
        model = User
        fields = ('email', 'password',)
