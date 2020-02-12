from django.test import TestCase
from django.db.models.signals import post_save

import factory

from .factories import UserFactory


class TestUser(TestCase):
    @factory.django.mute_signals(post_save)
    def test__user_str_representation_to_be_email(self):
        user = UserFactory(email="user@example.com")
        self.assertEqual(str(user), user.email)
