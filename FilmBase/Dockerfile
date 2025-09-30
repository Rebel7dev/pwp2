# Użyj oficjalnego obrazu Python
FROM python:3.10-slim-bookworm

# Zaktualizuj pakiety systemowe dla bezpieczeństwa
RUN apt-get update && apt-get upgrade -y && apt-get clean

ENV PYTHONUNBUFFERED=1

# Ustaw katalog roboczy
WORKDIR /app

# Skopiuj plik z zależnościami i zainstaluj je
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Skopiuj resztę kodu aplikacji
COPY . .

# Ustaw zmienną środowiskową i odsłoń port
ENV FLASK_APP=main.py
EXPOSE 5000

# Polecenie do uruchomienia bazy i aplikacji
CMD ["sh", "-c", "flask db upgrade && flask run --host=0.0.0.0"]