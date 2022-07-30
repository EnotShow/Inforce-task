import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


def _add_user():
    """ adding a user for test tasks """
    user = User(username='admin', email='admin@gmail.com')
    user.set_password('admin')
    user.save()
    return user


@pytest.mark.django_db
def test_my_user():
    _add_user()

    me = User.objects.get(username='admin')
    assert me


@pytest.mark.django_db
def test_user_auth():
    user = _add_user()

    client = APIClient()
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    assert client
