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

    def test_email_for_lowercase(self):
        """lowerCases"""
        email='test@rajeEv.com'
        user = get_user_model().objects.create_user(
            email=email,
            password='125478963@#5$!QWERty'
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'pass123')
    
    def test_create_superuser(self):
        """create a su"""
        user = get_user_model().objects.create_superuser(
            'rajeev@rajeevinc.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

