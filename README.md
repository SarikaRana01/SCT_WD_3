# Online Quiz System

A Django-based Online Quiz System where users can register, login, and take quizzes across multiple categories with scoring and timer functionality.

---

## Features

- User authentication (signup, login, logout)
- Category-based quizzes
- Multiple-choice questions (4 options, 1 correct)
- Timer for each quiz
- User score tracking and display
- Admin panel for managing quizzes and categories

---

## Setup Instructions

1. **Clone the repo**
```bash
git clone https://github.com/<username>/<repo>.git
cd <repo>
Create virtual environment

bash
Copy code
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
Install dependencies

bash
Copy code
pip install -r requirements.txt
Migrate database

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Create superuser

bash
Copy code
python manage.py createsuperuser
Load quiz data

bash
Copy code
python manage.py loaddata fixtures/quizdata.json
Run the server

bash
Copy code
python manage.py runserver
Access the app at http://127.0.0.1:8000/

Screenshots
Home / Dashboard

Quiz Page with Timer

Score Page

Admin Panel

Notes
The fixtures/quizdata.json contains quiz categories, questions, and answers.

Timer duration is set per category.

Sensitive info like SECRET_KEY should be stored in .env (do not push to GitHub)
