# HC - Django Project with LTE Admin Theme

A modern Django web application with authentication system and AdminLTE theme integration.

## Features

- **Authentication System**: Login, logout, and dashboard functionality
- **LTE Admin Theme**: Professional admin interface with modern design
- **Security**: Environment variables support and secret detection
- **Testing**: Comprehensive test suite with 100% coverage
- **Git Workflow**: Feature branch development workflow

## Quick Start

### Prerequisites

- Python 3.8+
- Virtual environment (recommended)

### Installation

1. **Clone and Setup**:
   ```bash
   git clone https://github.com/xavergig/hc.git
   cd hc
   ```

2. **Create Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**:
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

5. **Database Setup**:
   ```bash
   python manage.py migrate
   ```

6. **Create Superuser**:
   ```bash
   python manage.py createsuperuser
   ```

7. **Collect Static Files**:
   ```bash
   python manage.py collectstatic
   ```

### Running the Application

1. **Start Development Server**:
   ```bash
   python manage.py runserver
   ```

2. **Access URLs**:
   - Application: http://127.0.0.1:8000/
   - Login: http://127.0.0.1:8000/auth/login/
   - Dashboard: http://127.0.0.1:8000/auth/dashboard/
   - Admin Panel: http://127.0.0.1:8000/admin/

### Default Credentials

- **Username**: `admin`
- **Password**: `admin123`

## Development Workflow

### Running Tests

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test authentication

# Run with coverage
coverage run --source='.' manage.py test
coverage report
coverage html  # Generate HTML report
```

### Git Workflow

```bash
# Create feature branch
git checkout -b feature/your-feature-name

# Make changes and test
git add .
git commit -m "Your feature description"

# Push to GitHub
git push -u origin feature/your-feature-name

# Merge to main (when ready)
git checkout main
git merge feature/your-feature-name
git push origin main
```

## Project Structure

```
hc/
├── authentication/           # Authentication app
│   ├── views.py          # Login, logout, dashboard views
│   ├── forms.py          # Authentication forms
│   ├── templates/        # HTML templates
│   └── tests.py          # Test suite
├── hc_project/            # Django project settings
│   ├── settings.py        # Project configuration
│   └── urls.py           # URL routing
├── staticfiles/            # Collected static files (gitignored)
├── venv/                  # Virtual environment (gitignored)
└── .env                   # Environment variables (gitignored)
```

## Security Features

- **Environment Variables**: All secrets managed via `.env` file
- **Secret Detection**: Pre-commit hooks prevent secret commits
- **CSRF Protection**: Built-in Django CSRF middleware
- **Password Validation**: Django's secure password validators

## Testing

The project maintains 100% test coverage across all features:

- Authentication flows (login, logout, dashboard access)
- Form validation and error handling
- URL routing and redirects
- Template rendering and context

## Contributing

1. Create feature branches from `main`
2. Write tests for new functionality
3. Ensure 100% test coverage
4. Follow the existing code style
5. Submit pull requests for review

## License

This project is open source and available under the MIT License.
