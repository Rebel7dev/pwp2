#!/bin/sh

# Ustawia zmienną środowiskową dla komend 'flask'
export FLASK_APP=main.py

# Sprawdza, czy folder 'migrations' istnieje
if [ ! -d "migrations" ]; then
  echo "Folder 'migrations' nie znaleziony. Inicjalizuję bazę danych..."
  flask db init
  flask db migrate -m "Initial migration from Docker"
  flask db upgrade
else
  echo "Folder 'migrations' znaleziony. Stosuję migracje..."
  flask db upgrade
fi

echo "Uruchamiam aplikację..."
# Uruchamia główną komendę przekazaną z Dockerfile (czyli 'flask run...')
exec "$@"