import pytest
from rest_framework.test import APIClient
from rest_framework import status
from users.models import User


@pytest.fixture
def api_client():
    """create an instance of APIClient for making requests"""
    return APIClient()


@pytest.fixture
def user():
    """create a test user obj"""
    return User.objects.create_user(
        email='testuser@example.com',
        password='password123'
    )


@pytest.fixture
def admin_user():
    """create a superuser for testing admin func"""
    return User.objects.create_superuser(
        email='admin@example.com',
        password='adminpassword'
    )


@pytest.mark.django_db
def test_user_create(api_client):
    data = {
        'email': 'newuser@example.com',
        'password': 'newpassword',
    }
    response = api_client.post('/users/signup/', data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert User.objects.count() == 1  # Check that a new user was created
    assert User.objects.get().email == 'newuser@example.com'


@pytest.mark.django_db
def test_user_list(api_client, user, admin_user):
    api_client.force_authenticate(user=admin_user)  # authenticated as the admin user
    response = api_client.get('/users/list/')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2  # check that we have 2 users
    assert response.data[0]['email'] == user.email
    assert response.data[1]['email'] == admin_user.email


@pytest.mark.django_db
def test_user_update(api_client, user, admin_user):
    api_client.force_authenticate(user=admin_user)
    data = {
        'email': 'newtest@test.test'
    }
    response = api_client.patch(f'/users/update/{admin_user.id}/', data, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['email'] == 'newtest@test.test'


@pytest.mark.django_db
def test_user_update_not_authenticated(api_client, user):
    data = {
        'email': 'newtest@test.test'
    }
    response = api_client.patch(f'/users/update/{user.id}/', data, format='json')
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_user_delete(api_client, user, admin_user):
    api_client.force_authenticate(user=admin_user)  # authenticate as the admin user
    response = api_client.delete(f'/users/delete/{user.id}/')
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert User.objects.count() == 1  # check that only one user remains


@pytest.mark.django_db
def test_user_delete_not_authenticated(api_client, user):
    response = api_client.delete(f'/users/delete/{user.id}/')
    assert response.status_code == status.HTTP_401_UNAUTHORIZED  # check that the request is forbidden
