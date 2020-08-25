from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        """ it is is a function that is ran before every test """
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="admin@londonappdev.com",
            password='password@123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@londonappdev.com',
            password='password@123',
            name='Test user full name'
        )

    def test_user_listed(self):
        """ Test that users are listed on user page """
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)  # res stands for response
        print("response of http request-------", res)

        self.assertContains(res, self.user.name)
        """ what `assertContains` it does is it checks that
            the HTTP response was HTTP 200 and that
            it looks into the actual content of this 'res'
        """
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)
        self.assertEquals(res.status_code, 200)

    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
