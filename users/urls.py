from django.urls import path

from users.apps import UsersConfig
from users.views import UserCreateAPIView, UserListAPIView, UserUpdateAPIView, UserDeleteAPIView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = UsersConfig.name

urlpatterns = [
    #  user CreateReadUpdateDelete(CRUD) urls
    path('signup/', UserCreateAPIView.as_view(), name='user-register'),
    path('list/', UserListAPIView.as_view(), name='user-list'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user-update'),
    path('delete/<int:pk>/', UserDeleteAPIView.as_view(), name='user-delete'),

    #  token jwt
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
