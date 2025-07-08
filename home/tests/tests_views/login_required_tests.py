from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from teamspace.models import Position

HOME_PAGE = reverse("home:index")
INVITE_PAGE = reverse("home:invite")
SETTINGS_PAGE = reverse("home:settings", kwargs={"pk": 1})

class LoginRequiredTests(TestCase):
    def setUp(self):
        self.client = Client()

    @staticmethod
    def create_user():
        user = get_user_model().objects.create_user(
            username="test_user",
            password="<PASSWORD>",
            position=Position.objects.create(name="<NAME>"),
        )

        return user

    def test_public_home_page(self):
        response = self.client.get(HOME_PAGE)
        self.assertEqual(response.status_code, 200)

    def test_private_home_page(self):
        user = self.create_user()
        self.client.force_login(user)

        response = self.client.get(HOME_PAGE)
        self.assertEqual(response.status_code, 200)

    def test_public_invite(self):
        response = self.client.get(INVITE_PAGE)
        self.assertNotEqual(response.status_code, 200)

    def test_private_invite(self):
        user = self.create_user()
        self.client.force_login(user)

        response = self.client.get(INVITE_PAGE)
        self.assertEqual(response.status_code, 200)

    def test_public_settings(self):
        user = self.create_user()

        response = self.client.get(SETTINGS_PAGE)
        self.assertNotEqual(response.status_code, 200)

    def test_private_settings(self):
        user = self.create_user()
        self.client.force_login(user)

        response = self.client.get(SETTINGS_PAGE)
        self.assertEqual(response.status_code, 200)
