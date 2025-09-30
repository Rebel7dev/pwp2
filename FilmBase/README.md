# FilmBase - Twoja Osobista Baza Filmów 🎬

FilmBase to aplikacja webowa napisana w Pythonie (Flask), która pozwala na wyszukiwanie filmów i tworzenie osobistych list do obejrzenia. Projekt wykorzystuje bazę danych SQLite oraz zewnętrzne API od The Movie Database (TMDB).



---

## Technologie

* **Backend:** Python 3.10, Flask
* **Baza Danych:** SQLite z Flask-SQLAlchemy i Flask-Migrate
* **Frontend:** HTML, CSS (bez frameworka JS)
* **API:** The Movie Database (TMDB)
* **Konteneryzacja:** Docker

---

## Uruchomienie Lokalne (dla deweloperów)

Ta metoda wymaga zainstalowanego Pythona 3.10+ na komputerze.

1.  **Sklonuj repozytorium:**
    ```bash
    git clone [https://github.com/Rebel7dev/pwp2.git](https://github.com/Rebel7dev/pwp2.git)
    cd pwp2
    ```

2.  **Stwórz i aktywuj środowisko wirtualne:**
    ```bash
    # Na Windows
    python -m venv venv
    Set-ExecutionPolicy RemoteSigned -Scope Process
    .\venv\Scripts\activate

    # Na macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Zainstaluj zależności:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Skonfiguruj zmienne środowiskowe:**
    Stwórz plik o nazwie `.env` w głównym folderze projektu i uzupełnij go według wzoru:
    ```
    SECRET_KEY='wygeneruj_wlasny_bezpieczny_klucz'
    TMDB_API_KEY='wklej_tutaj_swoj_klucz_api_z_serwisu_tmdb'
    ```

5.  **Stwórz bazę danych:**
    Użyj poniższych komend, aby stworzyć bazę danych i zastosować migracje.
    ```bash
    # Na Windows (PowerShell)
    $env:FLASK_APP = "main.py"
    flask db upgrade

    # Na macOS/Linux
    export FLASK_APP=main.py
    flask db upgrade
    ```

6.  **Uruchom aplikację:**
    ```bash
    flask run
    ```
    Aplikacja będzie dostępna pod adresem `http://127.0.0.1:5000`.

---

## Uruchomienie z Dockerem (zalecane) 🐳

Ta metoda jest najprostsza i wymaga jedynie zainstalowanego Dockera.

1.  **Sklonuj repozytorium:**
    ```bash
    git clone [https://github.com/Rebel7dev/pwp2.git](https://github.com/Rebel7dev/pwp2.git)
    cd pwp2
    ```

2.  **Skonfiguruj zmienne środowiskowe:**
    Stwórz plik `.env` (tak jak w metodzie lokalnej) i uzupełnij go swoimi kluczami (`SECRET_KEY` i `TMDB_API_KEY`).

3.  **Zbuduj obraz Dockera:**
    ```bash
    docker build -t filmbase .
    ```

4.  **Uruchom kontener:**
    ```bash
    docker run -p 5000:5000 --env-file .env filmbase
    ```
    Aplikacja będzie dostępna pod adresem `http://127.0.0.1:5000`. Baza danych zostanie stworzona automatycznie przy pierwszym uruchomieniu kontenera.