#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install requirements
pip install -r requirements.txt

# Collect static files (CSS/JS)
python manage.py collectstatic --no-input

# Run migrations (Veritabanını kur)
python manage.py migrate