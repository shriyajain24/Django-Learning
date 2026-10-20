# Django Learning

This repository is a collection of beginner-friendly Django exercises and mini-projects used to practice core concepts such as project setup, app creation, templates, URLs, views, models, migrations, and full-stack app development.

## Project Overview

The repository includes several learning modules, each focused on a different Django topic:

- Django app creation and templates
- Django shell usage
- Models and migrations
- A recipe project with multiple apps and templates

## Repository Structure

```text
Django-Learning/
├── .devcontainer/
├── .gitignore
├── README.md
├── requirements.txt
├── Django_AppCreation_And_Templates/
│   ├── Django/
│   ├── accounts/
│   ├── home/
│   ├── manage.py
│   └── ...
├── Django_Shell/
├── Models_and_Migration/
│   ├── account/
│   ├── home/
│   ├── myproject/
│   ├── manage.py
│   └── ...
├── Recipe_Project/
│   ├── core/
│   ├── home/
│   ├── public/
│   ├── templates/
│   ├── vege/
│   ├── local_data.py
│   ├── manage.py
│   └── ...
└── .
```

## Tech Stack

- Python
- Django
- SQLite
- HTML
- CSS (in project templates)

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/shriyajain24/Django-Learning.git
cd Django-Learning
```

2. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Navigate to a specific Django project folder and run the development server:

```bash
cd Django_AppCreation_And_Templates
python manage.py runserver
```

5. Open the app in your browser at:

```text
http://127.0.0.1:8000/
```

## Learning Modules

- Django_AppCreation_And_Templates: practice app creation, Django project structure, and template rendering.
- Django_Shell: experiments using the Django shell and queryset operations.
- Models_and_Migration: examples of models, database setup, and migrations.
- Recipe_Project: a more complete project involving recipe-related pages and templates.

## Notes

This repository is intended for learning Django fundamentals, experimenting with app organization, and building small real-world examples step by step.
