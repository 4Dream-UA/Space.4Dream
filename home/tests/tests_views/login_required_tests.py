from django.contrib.auth import get_user_model
from django.test import TestCase, Client

from teamspace.models import Position
from .pages import (
    HOME_PAGE, INVITE_PAGE, SETTINGS_PAGE,
    PROFILE_PAGE, USER_DETAIL_PAGE
)


class LoginRequiredTests(TestCase):
    def setUp(self):
        self.client = Client()

    @staticmethod
    def create_user() -> get_user_model:
        user = get_user_model().objects.create_user(
            username="test_user",
            password="<PASSWORD>",
            position=Position.objects.create(name="<NAME>"),
        )

        return user

    def test_public_home_page(self) -> None:
        response = self.client.get(HOME_PAGE)
        self.assertEqual(response.status_code, 200)

    def test_private_home_page(self) -> None:
        user = self.create_user()
        self.client.force_login(user)

        response = self.client.get(HOME_PAGE)
        self.assertEqual(response.status_code, 200)

    def test_public_invite(self) -> None:
        response = self.client.get(INVITE_PAGE)
        self.assertNotEqual(response.status_code, 200)

    def test_private_invite(self) -> None:
        user = self.create_user()
        self.client.force_login(user)

        response = self.client.get(INVITE_PAGE)
        self.assertEqual(response.status_code, 200)

    def test_public_settings(self) -> None:
        user = self.create_user()

        response = self.client.get(SETTINGS_PAGE)
        self.assertNotEqual(response.status_code, 200)

    def test_private_settings(self) -> None:
        user = self.create_user()
        self.client.force_login(user)

        response = self.client.get(SETTINGS_PAGE)
        self.assertEqual(response.status_code, 200)

    def test_public_profile(self) -> None:
        response = self.client.get(PROFILE_PAGE)
        self.assertNotEqual(response.status_code, 200)

    def test_private_profile(self) -> None:
        user = self.create_user()
        self.client.force_login(user)

        response = self.client.get(PROFILE_PAGE)
        self.assertEqual(response.status_code, 200)

    def test_public_user_detail(self) -> None:
        user = self.create_user()

        response = self.client.get(USER_DETAIL_PAGE)
        self.assertNotEqual(response.status_code, 200)

    def test_private_user_detail(self) -> None:
        user = self.create_user()
        self.client.force_login(user)

        response = self.client.get(USER_DETAIL_PAGE)
        self.assertEqual(response.status_code, 200)
