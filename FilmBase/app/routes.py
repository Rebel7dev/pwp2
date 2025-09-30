import requests
from flask import render_template, flash, redirect, url_for, request, current_app
from flask_login import current_user, login_user, logout_user, login_required

from app import db
from app.models import User, Movie

def register_routes(app):
    @app.route('/')
    @app.route('/index')
    @login_required
    def index():
        """Główna strona po zalogowaniu, wyświetla listy filmów."""
        to_watch_movies = Movie.query.filter_by(owner=current_user, watchlist='to_watch').all()
        watched_movies = Movie.query.filter_by(owner=current_user, watchlist='watched').all()
        return render_template('index.html', title='Home', to_watch_movies=to_watch_movies, watched_movies=watched_movies)

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        """Logika logowania użytkownika."""
        if current_user.is_authenticated:
            return redirect(url_for('index'))

        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            user = User.query.filter_by(username=username).first()

            if user is None or not user.check_password(password):
                flash('Nieprawidłowa nazwa użytkownika lub hasło!')
                return redirect(url_for('login'))

            login_user(user, remember=True)
            return redirect(url_for('index'))

        return render_template('login.html', title='Zaloguj się')

    @app.route('/logout')
    def logout():
        """Logika wylogowania użytkownika."""
        logout_user()
        return redirect(url_for('login'))

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        """Logika rejestracji nowego użytkownika."""
        if current_user.is_authenticated:
            return redirect(url_for('index'))

        if request.method == 'POST':
            username = request.form.get('username')
            email = request.form.get('email')
            password = request.form.get('password')

            if User.query.filter_by(username=username).first():
                flash('Ta nazwa użytkownika jest już zajęta!')
                return redirect(url_for('register'))

            if User.query.filter_by(email=email).first():
                flash('Ten adres email jest już używany!')
                return redirect(url_for('register'))

            new_user = User(username=username, email=email)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()

            flash('Rejestracja zakończona sukcesem! Możesz się teraz zalogować.')
            return redirect(url_for('login'))

        return render_template('register.html', title='Zarejestruj się')

    @app.route('/search', methods=['POST'])
    @login_required
    def search():
        """Wysyła zapytanie do TMDB API i wyświetla wyniki."""
        query = request.form.get('query')
        if not query:
            return redirect(url_for('index'))

        api_key = current_app.config['TMDB_API_KEY']
        url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={query}&language=pl-PL"
        response = requests.get(url)
        search_results = response.json().get('results', [])

        return render_template('search_results.html', title='Wyniki wyszukiwania', results=search_results)

    @app.route('/add_movie', methods=['POST'])
    @login_required
    def add_movie():
        """Dodaje wybrany film do bazy danych i przypisuje go do użytkownika."""
        tmdb_id = request.form.get('tmdb_id')
        title = request.form.get('title')
        poster_path = request.form.get('poster_path')
        watchlist = request.form.get('watchlist')

        existing_movie = Movie.query.filter_by(owner=current_user, tmdb_id=tmdb_id).first()
        if existing_movie:
            flash('Ten film już jest na jednej z Twoich list!')
            return redirect(url_for('index'))

        new_movie = Movie(tmdb_id=tmdb_id, title=title, poster_path=poster_path, watchlist=watchlist, owner=current_user)
        db.session.add(new_movie)
        db.session.commit()
        flash(f'Dodano "{title}" do listy!')
        return redirect(url_for('index'))

    @app.route('/remove_movie/<int:movie_id>', methods=['POST'])
    @login_required
    def remove_movie(movie_id):
        """Usuwa film z listy użytkownika."""
        movie = Movie.query.get_or_404(movie_id)
        if movie.owner != current_user:
            # Użytkownik próbuje usunąć film, który nie należy do niego
            flash('Brak autoryzacji!', 'error')
            return redirect(url_for('index'))

        db.session.delete(movie)
        db.session.commit()
        flash(f'Usunięto "{movie.title}" z Twojej listy.')
        return redirect(url_for('index'))

    @app.route('/movie/<int:tmdb_id>')
    @login_required
    def movie_details(tmdb_id):
        """Wyświetla stronę ze szczegółowymi informacjami o filmie."""
        api_key = current_app.config['TMDB_API_KEY']

        # Zapytanie do API o szczegóły filmu ORAZ o obsadę (credits)
        url = f"https://api.themoviedb.org/3/movie/{tmdb_id}?api_key={api_key}&language=pl-PL&append_to_response=credits"

        response = requests.get(url)

        # print(f"Status zapytania do TMDB: {response.status_code}")
        # print(f"Odpowiedź z TMDB: {response.json()}")

        if response.status_code != 200:
            # Jeśli film nie zostanie znaleziony, przekieruj na stronę główną
            flash('Nie udało się pobrać szczegółów filmu.', 'error')
            return redirect(url_for('index'))

        movie_data = response.json()

        # Wyciągamy tylko kilku pierwszych aktorów z obsady
        cast = movie_data.get('credits', {}).get('cast', [])[:5]

        return render_template('movie_details.html', title=movie_data['title'], movie=movie_data, cast=cast)