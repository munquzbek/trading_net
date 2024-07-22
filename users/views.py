from rest_framework import generics
from rest_framework.permissions import AllowAny

from users.models import User
from users.serializers import UserCreateSerializer, UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """Create view for User model"""
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        # setting hashed password and switching is_active True
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListAPIView(generics.ListAPIView):
    """List view for User model"""
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    """Update view for User model"""
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDeleteAPIView(generics.DestroyAPIView):
    """Delete view for User model"""
    queryset = User.objects.all()
