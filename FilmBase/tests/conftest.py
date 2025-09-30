import pytest
from app import create_app, db
from app.models import User, Movie
from config import TestConfig

@pytest.fixture(scope='module')
def test_app():
    """Tworzy instancję aplikacji Flask na potrzeby testów."""
    app = create_app(config_class=TestConfig)
    with app.app_context():
        db.create_all()
        yield app # Zwraca aplikację do testów
        db.drop_all() # Czyści bazę danych po zakończeniu testów

@pytest.fixture(scope='module')
def test_client(test_app):
    """Tworzy klienta testowego, który symuluje przeglądarkę."""
    return test_app.test_client()