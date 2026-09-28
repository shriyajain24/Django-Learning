# Django Learning

This repository is a beginner-friendly Django project used for learning and practicing core Django concepts such as app structure, templates, URLs, and views.

## Project Overview

The project contains a Django app named `home` and a supporting `accounts` app. It includes a simple page flow with:

- a home page rendered from a template
- a success page response
- Django URL routing setup
- a default SQLite database

## Repository Structure

```text
Django-Learning/
├── .gitignore
├── README.md
└── Django/
    ├── Django/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── accounts/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    ├── home/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    ��   ├── migrations/
    │   ├── models.py
    │   ├── templates/
    │   │   └── home/
    │   │       └── index.html
    │   ├── tests.py
    │   └── views.py
    ├── db.sqlite3
    └── manage.py
```

## Tech Stack

- Python
- Django
- SQLite
- HTML

## Getting Started

1. Navigate to the Django project folder:

```bash
cd Django
```

2. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate     # On Windows
```

3. Install dependencies:

```bash
pip install django
```

4. Run the development server:

```bash
python manage.py runserver
```

5. Open the app in your browser at:

```text
http://127.0.0.1:8000/
```

## App Behavior

- The root URL (`/`) renders the `home` page.
- The `/success-page/` route returns a simple success HTTP response.
- The admin interface is available at `/admin/`.

## Notes

This project is mainly intended for learning Django fundamentals and experimenting with project/app organization.
