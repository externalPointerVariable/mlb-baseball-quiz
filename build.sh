#!/bin/bash

# Navigate to the backend directory
cd backend

# Install the required Python packages
pip install -r requirements.txt

# Navigate to the mlb Django project directory
cd mlb

# Apply database migrations
python manage.py migrate

# Create a superuser if the CREATE_SUPERUSER environment variable is set
if [[ $CREATE_SUPERUSER ]]; then
  python manage.py createsuperuser --no-input --email "$DJANGO_SUPERUSER_EMAIL"
fi
