import pytest
from rest_framework.test import APIClient
from rest_framework import status
from network.models import Network
from users.models import User


@pytest.fixture
def network():
    """create a test network """
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
def another_network():
    """create another test network instance for testing different scenarios"""
    return Network.objects.create(
        name='Retail Network',
        email='retail@example.com',
        country='Country',
        city='City',
        street='Main St',
        house_number='1',
        type='I'
    )


@pytest.fixture
def user(network):
    """create a test user with a network"""
    return User.objects.create_user(
        email='test@example.com',
        password='password123',
        network=network,
    )


@pytest.fixture
def api_client():
    """create an instance of APIClient for making requests"""
    return APIClient()


@pytest.mark.django_db
def test_get_network_list_as_active_user(api_client, user, network, another_network):
    api_client.force_authenticate(user=user)
    response = api_client.get('/network/')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1  # user should only see the network they are associated with
    assert response.data[0]['name'] == network.name  # verify the network's name


@pytest.mark.django_db
def test_get_network_detail_as_active_user(api_client, user, network):
    api_client.force_authenticate(user=user)
    response = api_client.get(f'/network/{network.id}/')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == network.name  # verify the network's name


@pytest.mark.django_db
def test_get_network_detail_forbidden_for_other_network(api_client, user, another_network):
    api_client.force_authenticate(user=user)
    response = api_client.get(f'/network/{another_network.id}/')
    # print(response.data)
    # {'detail': ErrorDetail(string='No Network matches the given query.', code='not_found')}
    # this shows cuz func get_queryset in NetworkViewSet
    assert response.status_code == status.HTTP_404_NOT_FOUND  # user should not have access


@pytest.mark.django_db
def test_create_network_as_active_user(api_client, user, network):
    api_client.force_authenticate(user=user)
    data = {
        'name': 'New Network',
        'email': 'newnetwork@example.com',
        'country': 'Country',
        'city': 'City',
        'street': 'Third St',
        'house_number': '3',
        'type': 'R'
    }
    response = api_client.post('/network/', data, format='json')
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_update_network_as_active_user(api_client, user, network):
    api_client.force_authenticate(user=user)
    data = {
        'name': 'Updated Network Name'
    }
    response = api_client.patch(f'/network/{network.id}/', data, format='json')
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_delete_network_as_active_user(api_client, user, network):
    api_client.force_authenticate(user=user)
    response = api_client.delete(f'/network/{network.id}/')
    assert response.status_code == status.HTTP_204_NO_CONTENT

