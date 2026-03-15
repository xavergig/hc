from django.test import TestCase
from django.urls import reverse
from django.http import HttpResponse


class DjangoInstallationTest(TestCase):
    """Test to verify Django is properly installed and working"""
    
    def test_django_version(self):
        """Test that Django is installed and accessible"""
        import django
        self.assertIsNotNone(django.VERSION)
        self.assertEqual(django.__version__.split('.')[0], '4')
    
    def test_django_settings_loaded(self):
        """Test that Django settings are properly loaded"""
        from django.conf import settings
        self.assertTrue(settings.configured)
        self.assertEqual(settings.INSTALLED_APPS[0], 'django.contrib.admin')
    
    def test_database_connection(self):
        """Test that Django can connect to the database"""
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
        self.assertEqual(result[0], 1)
    
    def test_django_urls_configured(self):
        """Test that Django URL configuration is working"""
        from django.urls import resolve
        # Test that admin URL resolves
        resolver = resolve('/admin/')
        self.assertEqual(resolver.view_name, 'admin:index')


class BasicViewTest(TestCase):
    """Test basic Django view functionality"""
    
    def test_simple_view_response(self):
        """Test creating a simple HTTP response"""
        response = HttpResponse("Hello Django!")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(b"Hello Django!", response.content)
    
    def test_test_client_works(self):
        """Test that Django test client is working"""
        response = self.client.get('/admin/')
        # Should redirect to login page, not 404
        self.assertNotEqual(response.status_code, 404)
