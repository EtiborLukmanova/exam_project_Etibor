# Sweet Shop

A full-stack Django web app for browsing and reviewing sweets/candy products — built as an exam project. Includes user accounts, a product catalog with search and pagination, and a comment/rating system.

## Features

- **Custom user accounts** — registration, login/logout, and editable profiles (with profile photo) using a custom user model
- **Sweet catalog** — browse all sweets with search by name and pagination
- **Sweet detail pages** — view individual sweet info (name, description, company, price, image)
- **Comments & ratings** — logged-in users can leave a comment with a 1–5 star rating on any sweet, and edit/delete their own comments
- **Sweet management** — add, update, and delete sweet listings (currently open to any logged-in user — see improvements below)
- **Production-ready static/media handling** — WhiteNoise for static files, configurable database via `dj-database-url` (works with SQLite locally or Postgres in production)

## Tech stack

- Python, Django 5
- PostgreSQL (production) / SQLite (local development)
- WhiteNoise for static file serving
- Pillow for image handling
- Deployed on Render (via `dj-database-url` + `gunicorn`)

## Project structure

```
manage.py
src/                  # Project settings, root URL config
users/
  models.py           # CustomUser (extends AbstractUser with phone number, profile image)
  views.py            # Register, login, logout, profile view/update
sweets/
  models.py           # Sweets, CustomUserComment
  views.py            # List/detail/add/update/delete sweets, add/update/delete comments
templates/            # HTML templates for all views
```

## Setup

1. Create a virtual environment and install dependencies:
   ```
   python -m venv env
   source env/bin/activate   # on Windows: env\Scripts\activate
   pip install -r requirements.txt
   ```

2. Copy `.env.example` to `.env`. For local development, the default SQLite setting works out of the box — just set your own `SECRET_KEY`:
   ```
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

3. Run migrations:
   ```
   python manage.py migrate
   ```

4. Create an admin user:
   ```
   python manage.py createsuperuser
   ```

5. Run the server:
   ```
   python manage.py runserver
   ```

6. Visit `http://localhost:8000/` — you'll land on the login/home flow. Register a new account to browse and review sweets.

## Notes / possible improvements

- Sweet add/update/delete is currently open to any logged-in user rather than restricted to admins/staff — worth adding a permission check if this were a real product.
- No automated tests yet (`tests.py` files are placeholders) — would be a good next addition.
- The default profile image path (`media/user_default_image.png`) needs an actual placeholder image added to `media/` for new users without a photo.
- Media files (user uploads, sweet images) are gitignored — in production these should go to persistent/cloud storage (e.g. S3), since Render's filesystem isn't persistent across deploys.
