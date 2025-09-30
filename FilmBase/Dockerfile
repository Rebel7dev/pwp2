# Użyj oficjalnego obrazu Python
FROM python:3.10-slim-bookworm

# Aktualizuje pakiety systemowe
RUN apt-get update && \
    apt-get upgrade -y --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Wyłącza buforowanie wyjścia Pythona, aby logi pojawiały się natychmiast
ENV PYTHONUNBUFFERED=1

# Ustaw katalog roboczy
WORKDIR /app

# Skopiuj plik z zależnościami i zainstaluj je
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Skopiuj resztę kodu aplikacji, w tym skrypt
COPY . .

# Nadaj skryptowi uprawnienia do uruchamiania
RUN chmod +x entrypoint.sh

# Ustaw skrypt jako główny punkt wejścia (ENTRYPOINT) do kontenera
ENTRYPOINT ["/app/entrypoint.sh"]

# Ustaw domyślną komendę (CMD), która zostanie przekazana do skryptu
CMD ["flask", "run", "--host=0.0.0.0"]