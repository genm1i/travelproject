#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

# Собираем статику
python manage.py collectstatic --no-input

# Миграции (SQLite → Postgres)
python manage.py migrate