from django.test import TestCase, Client
from django.contrib.auth import get_user_model

from teamspace.models import Position
from .pages import (
    INVITE_PAGE
)


class UserPassesTests(TestCase):
    def setUp(self) -> None:
        client = Client()

    @staticmethod
    def create_user() -> get_user_model:
        user = get_user_model().objects.create_user(
            username="test_user",
            password="<PASSWORD>",
            position=Position.objects.create(name="<NAME>"),
        )

        return user

    def test_user_public_able(self) -> None:
        user = self.create_user()
        self.client.force_login(user)

        response = self.client.get(INVITE_PAGE)
        self.assertNotEqual(response.status_code, 200)


    def test_user_private_able(self) -> None:
        user = self.create_user()
        user.position = Position.objects.create(name="HR Manager")
        user.save()
        self.client.force_login(user)

        response = self.client.get(INVITE_PAGE)
        self.assertEqual(response.status_code, 200)
