# network/tests.py

import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from network.models import Network, Product

User = get_user_model()


@pytest.fixture
def network():
    """creating test network obj"""
    return Network.objects.create(
        name='Factory Network',
        email='factory@example.com',
        country='Country',
        city='City',
        street='Main St',
        house_number='1',
        type='F'
    )


@pytest.fixture
def active_user(network):
    """creating test active user"""
    user = User.objects.create_user(
        email='activeuser@example.com',
        password='password123',
        network=network,
    )
    return user


@pytest.fixture
def inactive_user(network):
    """creating inactive test user"""
    user = User.objects.create_user(
        email='inactiveuser@example.com',
        password='password123',
        network=network,
        is_active=False,
    )
    return user


@pytest.fixture
def product():
    #  creating test product
    return Product.objects.create(
        name='Test product',
        model='Test model',
        release_date='2024-07-22'
    )


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_get_product_list_as_active_user(api_client, active_user):
    api_client.force_authenticate(user=active_user)
    response = api_client.get('/product/')
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_get_product_list_as_inactive_user(api_client, inactive_user):
    api_client.force_authenticate(user=inactive_user)
    response = api_client.get('/product/')
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_create_product_as_active_user(api_client, active_user):
    api_client.force_authenticate(user=active_user)
    data = {'name': 'New Test Product', 'model': 'New Model', 'release_date': '2024-07-23'}
    response = api_client.post('/product/', data=data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Product.objects.filter(name='New Test Product').exists()


@pytest.mark.django_db
def test_create_product_as_inactive_user(api_client, inactive_user):
    api_client.force_authenticate(user=inactive_user)
    data = {'name': 'New Test Product', 'model': 'New Model', 'release_date': '2024-07-23'}
    response = api_client.post('/product/', data=data, format='json')
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_update_product_as_active_user(api_client, active_user, product):
    api_client.force_authenticate(user=active_user)
    data = {'name': 'Updated Product'}
    response = api_client.patch(f'/product/{product.id}/', data=data, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert Product.objects.get(id=product.id).name == 'Updated Product'


@pytest.mark.django_db
def test_update_product_as_inactive_user(api_client, inactive_user, product):
    api_client.force_authenticate(user=inactive_user)
    data = {'name': 'Updated Product'}
    response = api_client.patch(f'/product/{product.id}/', data=data, format='json')
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_delete_product_as_active_user(api_client, active_user, product):
    api_client.force_authenticate(user=active_user)
    response = api_client.delete(f'/product/{product.id}/')
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Product.objects.filter(id=product.id).exists()


@pytest.mark.django_db
def test_delete_product_as_inactive_user(api_client, inactive_user, product):
    api_client.force_authenticate(user=inactive_user)
    response = api_client.delete(f'/product/{product.id}/')
    assert response.status_code == status.HTTP_403_FORBIDDEN
