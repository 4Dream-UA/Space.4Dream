from django.test import TestCase
from home.forms import RegisterInviteForm


class RegisterInviteFormTests(TestCase):
    def test_form_has_expected_fields(self):
        form = RegisterInviteForm()
        expected_fields = ["username", "password1", "password2", "first_name", "last_name", "email", "position"]
        self.assertEqual(sorted(list(form.fields.keys())), sorted(expected_fields))
