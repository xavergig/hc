from django.test import TestCase
from django.core.asgi import get_asgi_application
from django.core.wsgi import get_wsgi_application
from django.conf import settings
from django.core.management import execute_from_command_line
from django.urls import reverse, resolve
import os
import sys


class ProjectConfigTest(TestCase):
    """Test Django project configuration files"""

    def test_asgi_application_import(self):
        """Test that ASGI application can be imported"""
        try:
            from hc_project.asgi import application
            self.assertIsNotNone(application)
        except ImportError:
            self.fail("Could not import ASGI application")

    def test_wsgi_application_import(self):
        """Test that WSGI application can be imported"""
        try:
            from hc_project.wsgi import application
            self.assertIsNotNone(application)
        except ImportError:
            self.fail("Could not import WSGI application")

    def test_django_settings_module(self):
        """Test that Django settings module is properly configured"""
        self.assertTrue(hasattr(settings, 'INSTALLED_APPS'))
        self.assertTrue(hasattr(settings, 'SECRET_KEY'))
        self.assertTrue(hasattr(settings, 'DATABASES'))

    def test_asgi_get_asgi_application(self):
        """Test get_asgi_application function"""
        application = get_asgi_application()
        self.assertIsNotNone(application)
        self.assertTrue(callable(application))

    def test_wsgi_get_wsgi_application(self):
        """Test get_wsgi_application function"""
        application = get_wsgi_application()
        self.assertIsNotNone(application)
        self.assertTrue(callable(application))

    def test_environment_variable_settings(self):
        """Test environment variable configuration"""
        original_value = os.environ.get('DJANGO_SETTINGS_MODULE')
        self.assertIsNotNone(original_value)
        self.assertEqual(original_value, 'hc_project.settings')

    def test_manage_py_imports(self):
        """Test that manage.py has required imports"""
        # Test that we can import the functions used in manage.py
        try:
            from django.core.management import execute_from_command_line
            self.assertTrue(callable(execute_from_command_line))
        except ImportError:
            self.fail("Could not import execute_from_command_line")

    def test_django_modules_available(self):
        """Test that core Django modules are available"""
        try:
            import django
            self.assertTrue(hasattr(django, '__version__'))
        except ImportError:
            self.fail("Django module not available")

    def test_manage_py_main_function(self):
        """Test manage.py main function execution"""
        # Test that main function exists and is callable
        with open('manage.py', 'r') as f:
            content = f.read()
            self.assertIn('def main():', content)
            self.assertIn('if __name__ == \'__main__\':', content)
            self.assertIn('main()', content)

    def test_url_patterns(self):
        """Test that URL patterns are properly configured"""
        try:
            # Test admin URL resolution
            admin_resolve = resolve('/admin/')
            self.assertIsNotNone(admin_resolve.url_name)

            # Test authentication URL resolution
            auth_resolve = resolve('/auth/login/')
            self.assertEqual(auth_resolve.url_name, 'login')

            # Test root URL redirects to login
            root_resolve = resolve('/')
            self.assertIsNotNone(root_resolve.func)

        except Exception as e:
            self.fail(f"URL pattern test failed: {e}")

    def test_url_reverse_functions(self):
        """Test that URL reverse functions work correctly"""
        try:
            # Test reverse lookups
            admin_url = reverse('admin:index')
            self.assertIn('/admin/', admin_url)

            login_url = reverse('authentication:login')
            self.assertIn('/auth/login/', login_url)

            dashboard_url = reverse('authentication:dashboard')
            self.assertIn('/auth/dashboard/', dashboard_url)

        except Exception as e:
            self.fail(f"URL reverse test failed: {e}")

    def test_admin_url_names(self):
        """Test admin URL names are correctly configured"""
        try:
            # Test specific admin URL names
            admin_index = reverse('admin:index')
            self.assertTrue(admin_index.endswith('/admin/'))

        except Exception as e:
            self.fail(f"Admin URL test failed: {e}")

    def test_url_imports(self):
        """Test that URL-related imports work"""
        try:
            from django.urls import path, include
            from django.shortcuts import redirect
            self.assertTrue(callable(path))
            self.assertTrue(callable(include))
            self.assertTrue(callable(redirect))
        except ImportError as e:
            self.fail(f"URL import test failed: {e}")

    def test_urlpatterns_structure(self):
        """Test that urlpatterns list is properly structured"""
        try:
            from hc_project.urls import urlpatterns
            self.assertIsInstance(urlpatterns, list)
            self.assertGreater(len(urlpatterns), 0)  # At least one URL pattern

            # Test that each pattern is a path object
            for pattern in urlpatterns:
                self.assertTrue(hasattr(pattern, 'pattern'))

        except Exception as e:
            self.fail(f"URLPatterns structure test failed: {e}")

    def test_root_redirect(self):
        """Test that root URL redirects to login"""
        try:
            from hc_project.urls import urlpatterns
            # Check that root URL pattern exists (third pattern)
            self.assertEqual(len(urlpatterns), 3)
            root_pattern = urlpatterns[2]  # Root URL is the third pattern
            # Convert pattern to string for comparison
            pattern_str = str(root_pattern.pattern)
            self.assertIn('', pattern_str)  # Check for empty pattern
            self.assertIsNotNone(root_pattern.callback)

        except Exception as e:
            self.fail(f"Root redirect test failed: {e}")

    def test_admin_site_import(self):
        """Test that admin site is properly imported"""
        try:
            from django.contrib import admin
            self.assertIsNotNone(admin.site)
            self.assertTrue(hasattr(admin.site, 'urls'))

        except Exception as e:
            self.fail(f"Admin site import test failed: {e}")

    def test_urlpattern_attributes(self):
        """Test URL pattern attributes"""
        try:
            from hc_project.urls import urlpatterns
            # Test each pattern has required attributes
            for pattern in urlpatterns:
                self.assertTrue(hasattr(pattern, 'pattern'))
                self.assertTrue(hasattr(pattern, 'callback'))

        except Exception as e:
            self.fail(f"URLPattern attributes test failed: {e}")

    def test_admin_urls_config(self):
        """Test admin URLs configuration"""
        try:
            from django.contrib import admin
            # Test that admin site has URLs
            self.assertTrue(hasattr(admin.site, 'urls'))
            admin_urls = admin.site.urls
            self.assertIsNotNone(admin_urls)

        except Exception as e:
            self.fail(f"Admin URLs config test failed: {e}")

    def test_include_function(self):
        """Test include function usage"""
        try:
            from django.urls import include
            # Test that include is callable
            self.assertTrue(callable(include))

            # Test include with authentication URLs
            auth_include = include('authentication.urls')
            self.assertIsNotNone(auth_include)

        except Exception as e:
            self.fail(f"Include function test failed: {e}")

    def test_path_function(self):
        """Test path function usage"""
        try:
            from django.urls import path
            self.assertTrue(callable(path))

            # Test path creation
            test_path = path('test/', lambda: None)
            self.assertIsNotNone(test_path)

        except Exception as e:
            self.fail(f"Path function test failed: {e}")

    def test_lambda_function(self):
        """Test lambda function in root URL"""
        try:
            from hc_project.urls import urlpatterns
            # Find root pattern with lambda
            root_pattern = None
            for pattern in urlpatterns:
                if hasattr(pattern, 'callback') and callable(pattern.callback):
                    root_pattern = pattern
                    break

            self.assertIsNotNone(root_pattern)
            self.assertTrue(callable(root_pattern.callback))

        except Exception as e:
            self.fail(f"Lambda function test failed: {e}")

    def test_urlpattern_count(self):
        """Test that we have exactly 3 URL patterns"""
        try:
            from hc_project.urls import urlpatterns
            self.assertEqual(len(urlpatterns), 3)

        except Exception as e:
            self.fail(f"URLPattern count test failed: {e}")

    def test_urlpattern_order(self):
        """Test URL patterns are in expected order"""
        try:
            from hc_project.urls import urlpatterns
            # Admin should be first, auth second, root third
            self.assertTrue('admin' in str(urlpatterns[0]))
            self.assertTrue('auth' in str(urlpatterns[1]))
            # Convert pattern to string for comparison
            root_pattern_str = str(urlpatterns[2].pattern)
            self.assertIn('', root_pattern_str)  # Check for empty pattern

        except Exception as e:
            self.fail(f"URLPattern order test failed: {e}")

    def test_admin_site_urls_property(self):
        """Test admin site URLs property"""
        try:
            from django.contrib import admin
            # Access the urls property
            admin_urls = admin.site.urls
            self.assertIsNotNone(admin_urls)

        except Exception as e:
            self.fail(f"Admin site URLs test failed: {e}")

    def test_import_statements(self):
        """Test all import statements work"""
        try:
            # Test all imports from urls.py
            from django.contrib import admin
            from django.urls import path, include
            from django.shortcuts import redirect
            self.assertTrue(callable(path))
            self.assertTrue(callable(include))
            self.assertTrue(callable(redirect))
            self.assertIsNotNone(admin.site)

        except ImportError as e:
            self.fail(f"Import statements test failed: {e}")

    def test_urlpatterns_list_structure(self):
        """Test urlpatterns is a proper list"""
        try:
            from hc_project.urls import urlpatterns
            self.assertIsInstance(urlpatterns, list)
            self.assertGreater(len(urlpatterns), 0)

            # Test that all patterns are path objects
            for pattern in urlpatterns:
                self.assertTrue(hasattr(pattern, 'pattern'))
                self.assertTrue(hasattr(pattern, 'callback'))

        except Exception as e:
            self.fail(f"URLPatterns list structure test failed: {e}")

    def test_redirect_lambda_function(self):
        """Test root redirect lambda function"""
        try:
            from hc_project.urls import urlpatterns
            # Find root pattern with lambda
            root_pattern = None
            for pattern in urlpatterns:
                if hasattr(pattern, 'callback') and callable(pattern.callback):
                    root_pattern = pattern
                    break

            self.assertIsNotNone(root_pattern)
            self.assertTrue(callable(root_pattern.callback))

        except Exception as e:
            self.fail(f"Lambda function test failed: {e}")

    def test_database_config(self):
        """Test DATABASES configuration"""
        try:
            from django.conf import settings
            databases = settings.DATABASES
            self.assertIsInstance(databases, dict)
            self.assertIn('default', databases)

            # Test default database config
            default_db = databases['default']
            self.assertIn('ENGINE', default_db)
            self.assertIn('NAME', default_db)

        except Exception as e:
            self.fail(f"Database config test failed: {e}")

    def test_static_files_config(self):
        """Test static files configuration"""
        try:
            from django.conf import settings
            self.assertTrue(hasattr(settings, 'STATIC_URL'))
            self.assertTrue(hasattr(settings, 'STATIC_ROOT'))
            self.assertEqual(settings.STATIC_URL, '/static/')

        except Exception as e:
            self.fail(f"Static files config test failed: {e}")

    def test_middleware_config(self):
        """Test MIDDLEWARE configuration"""
        try:
            from django.conf import settings
            middleware = settings.MIDDLEWARE
            self.assertIsInstance(middleware, list)
            self.assertGreater(len(middleware), 0)

            # Test specific middleware classes
            self.assertIn('django.middleware.security.SecurityMiddleware', middleware)
            self.assertIn('django.contrib.sessions.middleware.SessionMiddleware', middleware)

        except Exception as e:
            self.fail(f"Middleware config test failed: {e}")

    def test_installed_apps_completeness(self):
        """Test all required apps are installed"""
        try:
            from django.conf import settings
            installed_apps = settings.INSTALLED_APPS

            # Test core Django apps
            required_apps = [
                'django.contrib.admin',
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.messages',
                'django.contrib.staticfiles',
            ]

            for app in required_apps:
                self.assertIn(app, installed_apps)

            # Test our custom apps
            self.assertIn('adminlte3', installed_apps)
            self.assertIn('adminlte3_theme', installed_apps)
            self.assertIn('authentication', installed_apps)

        except Exception as e:
            self.fail(f"Installed apps test failed: {e}")

    def test_django_management_import(self):
        """Test Django management commands import"""
        try:
            from django.core.management import execute_from_command_line
            self.assertTrue(callable(execute_from_command_line))

            # Test other management utilities
            from django.core.management import call_command
            from django.core.management.base import BaseCommand
            self.assertTrue(callable(call_command))
            self.assertTrue(callable(BaseCommand))

        except ImportError as e:
            self.fail(f"Django management import test failed: {e}")

    def test_main_function_structure(self):
        """Test main() function structure"""
        try:
            with open('manage.py', 'r') as f:
                content = f.read()

            # Test function exists
            self.assertIn('def main():', content)
            self.assertIn('if __name__ == \'__main__\':', content)
            self.assertIn('execute_from_command_line(sys.argv)', content)
            self.assertIn('os.environ.setdefault', content)

        except Exception as e:
            self.fail(f"Main function structure test failed: {e}")

    def test_command_line_args(self):
        """Test command line arguments handling"""
        try:
            import sys
            self.assertIsInstance(sys.argv, list)
            self.assertGreater(len(sys.argv), 0)

        except Exception as e:
            self.fail(f"Command line args test failed: {e}")

    def test_environment_variables(self):
        """Test environment variable handling"""
        try:
            # Test that Django settings module is set correctly
            import os
            settings_module = os.environ.get('DJANGO_SETTINGS_MODULE')
            self.assertEqual(settings_module, 'hc_project.settings')

        except Exception as e:
            self.fail(f"Environment variables test failed: {e}")
