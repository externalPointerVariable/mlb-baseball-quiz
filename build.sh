#!/bin/bash
set -e

echo "Navigating to backend directory..."
cd backend

echo "Installing Python dependencies..."
pip install -r requirements.txt

echo "Navigating to mlb directory..."
cd mlb

echo "Applying database migrations..."
python manage.py migrate

if [[ $CREATE_SUPERUSER ]]; then
  echo "Creating Django superuser..."
  python manage.py createsuperuser --no-input --email "$DJANGO_SUPERUSER_EMAIL"
fi

echo "Build script completed successfully!"
