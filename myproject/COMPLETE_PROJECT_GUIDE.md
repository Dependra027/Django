# Django Project - Complete Reference Guide

## 📋 Table of Contents
1. [Project Overview](#project-overview)
2. [Environment Setup](#environment-setup)
3. [Project Structure](#project-structure)
4. [Step-by-Step Implementation](#step-by-step-implementation)
5. [Testing Procedures](#testing-procedures)
6. [Troubleshooting Guide](#troubleshooting-guide)
7. [Quick Commands Reference](#quick-commands-reference)
8. [Future Development](#future-development)

---

## 🎯 Project Overview

**What This Project Demonstrates:**
- Django project setup and configuration
- Creating and managing Django apps
- URL routing and view handling
- Template system implementation
- Static files management
- Custom error page handling
- Development vs production settings

**Technologies Used:**
- Python 3.13.7
- Django 5.2.6
- SQLite3 database
- HTML/CSS for frontend
- PowerShell for Windows development

---

## 🔧 Environment Setup

### Step 1: Virtual Environment Setup
```powershell
# Navigate to your practice directory
cd C:\Users\depen\django\practice

# Create virtual environment
python -m venv menv

# Activate virtual environment (Windows)
menv\Scripts\activate

# Verify activation (you should see (menv) in your prompt)
```

### Step 2: Django Installation
```powershell
# Make sure you're in the activated virtual environment
pip install django

# Verify installation
python -c "import django; print(django.get_version())"
# Should output: 5.2.6
```

### Step 3: Project Creation
```powershell
# Create Django project
django-admin startproject myproject

# Navigate into project directory
cd myproject

# Verify project structure
dir
# Should see: manage.py, myproject/ folder
```

---

## 📁 Project Structure

### Complete File Structure
```
myproject/
├── manage.py                    # Django management script
├── db.sqlite3                   # SQLite database (created after migrations)
├── myproject/                   # Main project directory
│   ├── __init__.py
│   ├── settings.py              # Django settings
│   ├── urls.py                  # Main URL configuration
│   ├── views.py                 # Main project views
│   ├── wsgi.py                  # WSGI configuration
│   └── asgi.py                  # ASGI configuration
├── chai/                        # Custom Django app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── tests.py
│   ├── templates/               # App-specific templates
│   │   ├── chai.html
│   │   └── identity.html
│   └── migrations/              # Database migrations
│       ├── __init__.py
│       └── (migration files)
├── templates/                   # Global templates
│   ├── index.html
│   └── 404.html
└── static/                      # Static files
    └── style.css
```

---

## 🚀 Step-by-Step Implementation

### Phase 1: Basic Project Setup

#### Step 1: Create Main Views
**File:** `myproject/myproject/views.py`
```python
from django.shortcuts import render
from django.http import HttpResponse

def member(request):
    return HttpResponse("Hello, Dependra")

def home(request):
    return HttpResponse("Hello, World!")

def about(request):
    return HttpResponse("This is the about page.")

def contact(request):
    return HttpResponse("This is the contact page.")

def home_template(request):
    return render(request, 'index.html')

def custom_404(request, exception):
    return render(request, '404.html', status=404)
```

#### Step 2: Configure Main URLs
**File:** `myproject/myproject/urls.py`
```python
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('member/', views.member, name='member'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('template/', views.home_template, name='template'),
    path('chai/', include('chai.urls')),
]

# Custom error handlers
handler404 = 'myproject.views.custom_404'
```

#### Step 3: Configure Settings
**File:** `myproject/myproject/settings.py`
```python
# Key settings to configure:

# Template directories
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Add this line
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Static files
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Installed apps (add your custom app)
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'chai',  # Add your custom app here
]
```

### Phase 2: Create Custom Django App

#### Step 1: Create the App
```powershell
# Make sure you're in the myproject directory
python manage.py startapp chai
```

#### Step 2: Configure App URLs
**File:** `myproject/chai/urls.py` (create this file)
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.chai_view, name='chai'),
    path('identity/', views.identity_view, name='identity'),
]
```

#### Step 3: Create App Views
**File:** `myproject/chai/views.py`
```python
from django.shortcuts import render
from django.http import HttpResponse

def chai_view(request):
    return render(request, 'chai.html')

def identity_view(request):
    return render(request, 'identity.html')
```

### Phase 3: Template System

#### Step 1: Create Global Templates Directory
```powershell
# Create templates directory in project root
mkdir templates
```

#### Step 2: Create Main Template
**File:** `myproject/templates/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Django Project</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
            text-align: center;
        }
        .nav-links {
            text-align: center;
            margin: 20px 0;
        }
        .nav-links a {
            margin: 0 10px;
            padding: 10px 20px;
            background-color: #007bff;
            color: white;
            text-decoration: none;
            border-radius: 5px;
        }
        .nav-links a:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to My Django Project!</h1>
        <div class="nav-links">
            <a href="/">Home</a>
            <a href="/member/">Member</a>
            <a href="/about/">About</a>
            <a href="/contact/">Contact</a>
            <a href="/chai/">Chai App</a>
        </div>
        <p>This is the main template rendered by Django.</p>
    </div>
</body>
</html>
```

#### Step 3: Create Custom 404 Template
**File:** `myproject/templates/404.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 - Page Not Found</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 100px;
            background-color: #f5f5f5;
        }
        .error-container {
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            background: white;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #e74c3c;
            font-size: 72px;
            margin: 0;
        }
        h2 {
            color: #333;
            margin: 20px 0;
        }
        p {
            color: #666;
            font-size: 18px;
            margin: 20px 0;
        }
        .back-link {
            display: inline-block;
            padding: 12px 24px;
            background-color: #3498db;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            font-weight: bold;
            margin-top: 20px;
        }
        .back-link:hover {
            background-color: #2980b9;
        }
    </style>
</head>
<body>
    <div class="error-container">
        <h1>404</h1>
        <h2>Oops! Page Not Found</h2>
        <p>The page you're looking for doesn't exist.</p>
        <p>Don't worry, it happens to the best of us!</p>
        <a href="/" class="back-link">Go Back Home</a>
    </div>
</body>
</html>
```

### Phase 4: Static Files

#### Step 1: Create Static Directory
```powershell
# Create static directory
mkdir static
```

#### Step 2: Create CSS File
**File:** `myproject/static/style.css`
```css
/* Global Styles */
body {
    font-family: 'Arial', sans-serif;
    line-height: 1.6;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

/* Navigation */
.nav {
    background-color: #333;
    padding: 10px 0;
    margin-bottom: 20px;
}

.nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
}

.nav li {
    margin: 0 15px;
}

.nav a {
    color: white;
    text-decoration: none;
    padding: 10px 15px;
    border-radius: 5px;
    transition: background-color 0.3s;
}

.nav a:hover {
    background-color: #555;
}

/* Content */
.content {
    background: white;
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

/* Responsive Design */
@media (max-width: 768px) {
    .nav ul {
        flex-direction: column;
        text-align: center;
    }
    
    .nav li {
        margin: 5px 0;
    }
    
    .container {
        padding: 10px;
    }
}
```

---

## 🧪 Testing Procedures

### Basic Functionality Testing

#### Step 1: Start Development Server
```powershell
# Navigate to project directory
cd C:\Users\depen\django\practice\myproject

# Start server
python manage.py runserver

# Server should start on http://127.0.0.1:8000/
```

#### Step 2: Test All URL Endpoints
Open browser and test these URLs:

1. **Home Page**: `http://127.0.0.1:8000/`
   - Expected: "Hello, World!"

2. **Member Page**: `http://127.0.0.1:8000/member/`
   - Expected: "Hello, Dependra"

3. **About Page**: `http://127.0.0.1:8000/about/`
   - Expected: "This is the about page."

4. **Contact Page**: `http://127.0.0.1:8000/contact/`
   - Expected: "This is the contact page."

5. **Template Page**: `http://127.0.0.1:8000/template/`
   - Expected: Rendered index.html template

6. **Chai App**: `http://127.0.0.1:8000/chai/`
   - Expected: Chai app functionality

### Custom 404 Testing

#### Step 1: Enable Custom 404
**File:** `myproject/myproject/settings.py`
```python
DEBUG = False  # Change from True to False
ALLOWED_HOSTS = ['localhost', '127.0.0.1']  # Add this line
```

#### Step 2: Test Custom 404
```powershell
# Test with PowerShell
Invoke-WebRequest -Uri "http://127.0.0.1:8000/nonexistent-page/" -UseBasicParsing

# Or visit in browser: http://127.0.0.1:8000/any-fake-url/
# Should show custom 404 page
```

#### Step 3: Verify Server Logs
Look for entries like:
```
[27/Sep/2025 22:49:57] "GET /any-fake-page HTTP/1.1" 404 1571
```
The large byte count (1571) indicates the custom template is rendering.

---

## 🔧 Troubleshooting Guide

### Common Issues and Solutions

#### Issue 1: "No such file or directory: manage.py"
**Problem**: Running commands from wrong directory
**Solution**:
```powershell
# Navigate to correct directory
cd C:\Users\depen\django\practice\myproject

# Verify you're in the right place
dir manage.py
# Should show manage.py file
```

#### Issue 2: "Could not import custom handler404"
**Problem**: Import errors in views.py
**Solution**:
```python
# Check views.py has correct imports
from django.shortcuts import render
from django.http import HttpResponse

# Function signature must include exception parameter
def custom_404(request, exception):
    return render(request, '404.html', status=404)
```

#### Issue 3: Custom 404 not showing
**Problem**: DEBUG = True prevents custom error pages
**Solution**:
```python
# In settings.py
DEBUG = False  # Must be False for custom 404
ALLOWED_HOSTS = ['localhost', '127.0.0.1']  # Required when DEBUG=False
```

#### Issue 4: Template not found
**Problem**: Template directory not configured
**Solution**:
```python
# In settings.py TEMPLATES section
'DIRS': [BASE_DIR / 'templates'],  # Add this line
```

#### Issue 5: Static files not loading
**Problem**: Static files not configured
**Solution**:
```python
# In settings.py
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
```

#### Issue 6: PowerShell syntax errors
**Problem**: Using bash syntax in PowerShell
**Solution**:
```powershell
# Use PowerShell syntax
cd myproject; python manage.py runserver

# Instead of bash syntax
cd myproject && python manage.py runserver
```

### Server Management

#### Starting Server
```powershell
# Basic start
python manage.py runserver

# Start on specific port
python manage.py runserver 8080

# Start with specific IP and port
python manage.py runserver 127.0.0.1:8000
```

#### Stopping Server
- Press `Ctrl+C` in the terminal
- Or close the terminal window

#### Restarting After Changes
```powershell
# Stop server (Ctrl+C) then restart
python manage.py runserver
```

---

## ⚡ Quick Commands Reference

### Essential Django Commands
```powershell
# Create new Django project
django-admin startproject projectname

# Create new Django app
python manage.py startapp appname

# Run development server
python manage.py runserver

# Run database migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser for admin
python manage.py createsuperuser

# Check for errors
python manage.py check

# Collect static files (for production)
python manage.py collectstatic
```

### Navigation Commands
```powershell
# Navigate to project directory
cd C:\Users\depen\django\practice\myproject

# Navigate to parent directory
cd ..

# List directory contents
dir

# Create directory
mkdir foldername
```

### Virtual Environment Commands
```powershell
# Activate virtual environment
menv\Scripts\activate

# Deactivate virtual environment
deactivate

# Install package
pip install packagename

# List installed packages
pip list
```

---

## 🔮 Future Development

### Next Steps to Implement

#### 1. Database Models
```python
# In chai/models.py
from django.db import models

class ChaiVariant(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
```

#### 2. Forms
```python
# In chai/forms.py
from django import forms
from .models import ChaiVariant

class ChaiForm(forms.ModelForm):
    class Meta:
        model = ChaiVariant
        fields = ['name', 'price']
```

#### 3. Admin Interface
```python
# In chai/admin.py
from django.contrib import admin
from .models import ChaiVariant

admin.site.register(ChaiVariant)
```

#### 4. User Authentication
```python
# Add to settings.py
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
```

### Production Deployment Checklist

#### 1. Security Settings
```python
# In settings.py for production
DEBUG = False
SECRET_KEY = 'your-secret-key-here'
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

# Security middleware
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
```

#### 2. Static Files
```python
# In settings.py
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
```

#### 3. Database (Production)
```python
# Example PostgreSQL configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

## 📝 Notes and Tips

### Development Best Practices
1. **Always use virtual environments** for Python projects
2. **Keep DEBUG = True** during development
3. **Use DEBUG = False** only for testing custom error pages
4. **Test all URL endpoints** after making changes
5. **Check server logs** for error messages
6. **Use meaningful names** for views and URLs
7. **Organize templates** in logical directory structure

### Common Mistakes to Avoid
1. Running commands from wrong directory
2. Forgetting to add apps to INSTALLED_APPS
3. Not configuring template directories
4. Using bash syntax in PowerShell
5. Forgetting to restart server after settings changes
6. Not testing custom 404 with DEBUG = False

### Useful Resources
- [Django Official Documentation](https://docs.djangoproject.com/)
- [Django Tutorial](https://docs.djangoproject.com/en/stable/intro/tutorial01/)
- [Django Best Practices](https://django-best-practices.readthedocs.io/)

---

## 🎯 Project Status

**Current Status**: ✅ **FULLY FUNCTIONAL**

**Implemented Features**:
- ✅ Django project setup
- ✅ Custom Django app (chai)
- ✅ Multiple views and URL routing
- ✅ Template system with global templates
- ✅ Static files configuration
- ✅ Custom 404 error handling
- ✅ Development environment setup

**Ready for**:
- Database models implementation
- User authentication
- Production deployment
- Additional features and apps

---

*Last Updated: September 27, 2025*
*Django Version: 5.2.6*
*Python Version: 3.13.7*
