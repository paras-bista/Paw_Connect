#!/bin/bash

echo "🚀 Starting Paw-Connect deployment on Azure..."

# Navigate to project directory
cd /home/site/wwwroot

# Run database migrations
echo "📊 Running database migrations..."
python manage.py migrate --noinput

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput --clear

# Create cache tables if needed
echo "💾 Creating cache tables..."
python manage.py createcachetable || true

echo "✅ Startup complete! Application is ready."

# Start Gunicorn (handled by Procfile, this is just for reference)
# gunicorn Pawconnect.wsgi:application --bind 0.0.0.0:8000 --workers 3
