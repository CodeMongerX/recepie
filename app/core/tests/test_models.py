from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_user_with_email_successful(self):
        """Testing"""
        email = 'test@rajeevinc.com'
        password='125478963@#5$!QWERty'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

