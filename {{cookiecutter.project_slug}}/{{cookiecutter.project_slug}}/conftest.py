from django.test import RequestFactory

import pytest

from {{ cookiecutter.project_slug }}.accounts.models import User
from {{ cookiecutter.project_slug }}.accounts.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    return UserFactory()


@pytest.fixture
def request_factory() -> RequestFactory:
    return RequestFactory()
