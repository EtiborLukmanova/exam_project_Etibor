from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from users.models import CustomUser


class SignUpLoginProfileTests(TestCase):

    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'StrongPassword123'
        }
        User.objects.create_user(**self.user_data)

    def test_successful_registration(self):
        response = self.client.post(reverse('signup'), self.user_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))

    def test_duplicate_user_information(self):
        response = self.client.post(reverse('signup'), self.user_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This username or email is already in use.')

    def test_weak_password(self):
        weak_password_data = self.user_data.copy()
        weak_password_data['password'] = 'weak'
        response = self.client.post(reverse('signup'), weak_password_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Password is too weak.')

    def test_successful_login(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'StrongPassword123'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('profile'))

    def test_access_profile_page_after_login(self):
        self.client.login(username='testuser', password='StrongPassword123')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome, testuser!')

    def test_create_read_update_delete_record(self):
        item_data = {'name': 'New Item', 'description': 'Description', 'price': 10.99}
        response = self.client.post(reverse('create_item'), item_data)
        self.assertEqual(response.status_code, 302)

        item_id = CustomUser.objects.latest('id').id
        response = self.client.get(reverse('view_item', args=[item_id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New Item')

        updated_item_data = {'name': 'Updated Item', 'description': 'Updated Description', 'price': 15.99}
        response = self.client.post(reverse('update_item', args=[item_id]), updated_item_data)
        self.assertEqual(response.status_code, 302)

        # Delete
        response = self.client.post(reverse('delete_item', args=[item_id]))
        self.assertEqual(response.status_code, 302)

