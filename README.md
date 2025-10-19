# Dynamic Profile Endpoint

## Simple RESTful API endpoint that returns my profile

A RESTful API endpoint that returns user profile information(my information) along with dynamic cat facts from an external API.

## 🚀 Features

- GET endpoint at `/me` that returns profile data
- Real-time UTC timestamp generation
- Dynamic cat facts fetched from Cat Facts API
- Robust error handling for external API failures
- CORS enabled for cross-origin requests

## 📋 Prerequisites

- Python 3.10 or higher
- pip (Python package installer)
- Git

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/kim-mkuu/hng-stage0.git
cd hng-stage0
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment

# On Windows:
venv\Scripts\activate

# On Linux/Mac:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
# Upgrade pip
pip install --upgrade pip

# Install required packages
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```bash
touch .env
```

Add the following variables to `.env`:

```.env
SECRET_KEY=your-django-secret-key-here
DEBUG=True
CAT_FACTS_API_URL=https://catfact.ninja/fact
CAT_FACTS_API_TIMEOUT=5
```

**Note:** Generate a secure SECRET_KEY using:

```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 5. Apply Migrations

```bash
python manage.py migrate
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

The API will be available at: `http://127.0.0.1:8000/me`

## 📦 Dependencies

The project uses the following Python packages:

- **Django** (5.1.2) - Web framework
- **djangorestframework** (3.15.2) - REST API framework
- **requests** (2.32.3) - HTTP library for external API calls
- **python-dotenv** (1.0.1) - Environment variable management
- **django-cors-headers** (4.5.0) - CORS handling
- **gunicorn** (23.0.0) - Production WSGI server
- **whitenoise** (6.8.2) - Static file serving

### Installing Dependencies

All dependencies are listed in `requirements.txt`. Install them using:

```bash
pip install -r requirements.txt
```

To install individual packages:

```bash
pip install django djangorestframework requests python-dotenv django-cors-headers
```

For production deployment, also install:

```bash
pip install gunicorn whitenoise
```

## 🌐 API Endpoint

### GET /me

Returns user profile information with a dynamic cat fact.

**Live Endpoint:**

```link
API View: https://hng-stage0-production-d56a.up.railway.app/me?format=api

JSON Response: https://hng-stage0-production-d56a.up.railway.app/me?format=json
```

**Response Format:**

```json
{
  "status": "success",
  "user": {
    "email": "your-email@example.com",
    "name": "Your Full Name",
    "stack": "Python/Django"
  },
  "timestamp": "2025-10-19T14:30:45.123Z",
  "fact": "Cats sleep 70% of their lives."
}
```

**Status Codes:**

- `200 OK` - Success

## 🔧 Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `SECRET_KEY` | Django secret key for security | Yes | - |
| `DEBUG` | Enable/disable debug mode | No | False |
| `CAT_FACTS_API_URL` | Cat Facts API endpoint | No | https://catfact.ninja/fact |
| `CAT_FACTS_API_TIMEOUT` | API request timeout (seconds) | No | 5 |

## 🚢 Deployment

### Railway Deployment

1. Push code to GitHub
2. Sign up at [railway.app](https://railway.app)
3. Create new project from GitHub repo
4. Add environment variables in Railway dashboard
5. Set `DEBUG=False` for production
6. Railway will auto-deploy

### Environment Variables for Production

```env
SECRET_KEY=your-production-secret-key
DEBUG=False
CAT_FACTS_API_URL=https://catfact.ninja/fact
CAT_FACTS_API_TIMEOUT=5
```

## 🧪 Testing

Test the endpoint locally:

```bash
# Using curl
curl http://127.0.0.1:8000/me

# Using browser
Open: http://127.0.0.1:8000/me
```

Test the deployed endpoint:

```bash
curl https://your-app.up.railway.app/me
```

## 📁 Project Structure

```txt
hng-stage0/
├── api/
│   ├── __init__.py
│   ├── views.py          # API endpoint logic
│   ├── urls.py           # API URL routing
│   └── apps.py
├── profile_api/
│   ├── __init__.py
│   ├── settings.py       # Django settings
│   ├── urls.py           # Main URL configuration
│   └── wsgi.py
├── .env                  # Environment variables (not in repo)
├── .gitignore
├── manage.py
├── requirements.txt      # Python dependencies
├── Procfile             # Railway deployment config
├── runtime.txt          # Python version
└── README.md
```

## 🔗 Links

- [HNG Internship](https://hng.tech/internship)
- [Cat Facts API Documentation](https://catfact.ninja/)

## 🐛 Troubleshooting

### Common Issues

**Issue:** `ModuleNotFoundError: No module named 'rest_framework'`

- **Solution:** Install dependencies: `pip install -r requirements.txt`

**Issue:** `AssertionError: You must set settings.ALLOWED_HOSTS if DEBUG is False`

- **Solution:** Set `DEBUG=True` in `.env` for local development

**Issue:** Cat fact returns `null`

- **Solution:** Check internet connection and verify Cat Facts API is accessible

**Issue:** `SECRET_KEY` not found

- **Solution:** Ensure `.env` file exists and contains `SECRET_KEY`

## 👤 Author

kim-mkuu

## 📝 License

MIT
