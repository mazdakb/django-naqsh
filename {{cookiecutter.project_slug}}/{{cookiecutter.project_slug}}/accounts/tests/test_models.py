from django.test import TestCase
from django.db.models.signals import post_save

import factory

from .factories import UserFactory


class TestUser(TestCase):
    @factory.django.mute_signals(post_save)
    def test__str__(self):
        self.assertEqual(
            UserFactory(email="user1@exaple.com").__str__(), "user1@exaple.com"
        )
