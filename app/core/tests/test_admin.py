from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class adminSiteTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@rajeevinc.com',
            password='test@123'
        )
        self.client.force_login(user=self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='someuser@rajeevinc.com',
            password='test@123',
            name='someguy'
        )

    def test_user_listed(self):
        """Test users that are listed on thta page"""
        url = reverse("admin:core_user_changelist")
        response = self.client.get(url)

        self.assertContains(response, self.user.name)
        self.assertContains(response, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)