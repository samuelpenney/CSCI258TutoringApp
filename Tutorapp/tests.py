from django.test import TestCase
from django.urls import reverse


class SignUpPageTests(TestCase):
    def test_age_is_not_displayed_on_signup_page(self):
        response = self.client.get(reverse("signup"))

        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'name="age"')
