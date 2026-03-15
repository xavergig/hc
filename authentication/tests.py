from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages


class AuthenticationViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'  # pragma: allowlist secret
        )

    def test_login_view_get(self):
        """Test that login page loads correctly"""
        response = self.client.get(reverse('authentication:login'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Login')
        self.assertContains(response, 'csrfmiddlewaretoken')

    def test_login_view_post_valid(self):
        """Test successful login"""
        response = self.client.post(reverse('authentication:login'), {
            'username': 'testuser',
            'password': 'testpass123'  # pragma: allowlist secret
        })
        self.assertRedirects(response, reverse('authentication:dashboard'))

        # Check success message
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn('Welcome back', str(messages[0]))

    def test_login_view_post_invalid(self):
        """Test failed login"""
        response = self.client.post(reverse('authentication:login'), {
            'username': 'testuser',
            'password': 'wrongpass'  # pragma: allowlist secret
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid username or password')

    def test_logout_view(self):
        """Test logout functionality"""
        self.client.login(username='testuser', password='testpass123')  # pragma: allowlist secret
        response = self.client.get(reverse('authentication:logout'))
        self.assertRedirects(response, reverse('authentication:login'))

        # Check logout message
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn('Goodbye', str(messages[0]))

    def test_dashboard_view_authenticated(self):
        """Test dashboard access for authenticated user"""
        self.client.login(username='testuser', password='testpass123')  # pragma: allowlist secret
        response = self.client.get(reverse('authentication:dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Dashboard')
        self.assertContains(response, 'testuser')

    def test_dashboard_view_unauthenticated(self):
        """Test dashboard redirects unauthenticated user"""
        response = self.client.get(reverse('authentication:dashboard'))
        self.assertRedirects(response, f"{reverse('authentication:login')}?next=/auth/dashboard/")

    def test_login_redirects_authenticated_user(self):
        """Test that authenticated users are redirected from login"""
        self.client.login(username='testuser', password='testpass123')  # pragma: allowlist secret
        response = self.client.get(reverse('authentication:login'))
        self.assertRedirects(response, reverse('authentication:dashboard'))
