# tests/test_auth.py

from app.models import User

def test_registration(test_client):
    """
    GIVEN: A Flask application configured for testing
    WHEN: A POST request is sent to the '/register' route
    THEN: A new user should be created in the database
    """
    response = test_client.post('/register', data={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'password123'
    }, follow_redirects=True)

    assert response.status_code == 200
    assert 'Rejestracja zakończona sukcesem!' in response.data.decode('utf-8')

    user = User.query.filter_by(username='testuser').first()
    assert user is not None
    assert user.email == 'test@example.com'


def test_login_and_logout(test_client):
    """
    GIVEN: A user has been registered
    WHEN: A POST request is sent to the '/login' route with correct credentials
    THEN: The user should be logged in and then can log out
    """
    # Najpierw tworzymy użytkownika
    test_client.post('/register', data={
        'username': 'loginuser',
        'email': 'login@example.com',
        'password': 'password'
    })

    # Test logowania
    login_response = test_client.post('/login', data={
        'username': 'loginuser',
        'password': 'password'
    }, follow_redirects=True)

    assert login_response.status_code == 200
    assert 'Witaj, loginuser!' in login_response.data.decode('utf-8')

    # Test wylogowania
    logout_response = test_client.get('/logout', follow_redirects=True)
    assert logout_response.status_code == 200
    assert 'Zaloguj się' in logout_response.data.decode('utf-8')