from flask import Flask

"""
This module implements a simple Flask web application with the following routes:

Routes:
    /hello (GET):
        Returns a simple "Hello, World!" message.
    /user/<name> (GET):
        Greets the user by their name.
    / (GET):
        Displays the home page with links to the "About" page and the "Users" list.
    /about (GET):
        Provides information about the application and its creators.
    /users (GET):
        Displays a list of users with links to their individual details.
    /user/<int:user_id> (GET):
        Displays details of a specific user by their ID. If the user does not exist,
        returns a message indicating that the user does not exist.

Global Variables:
    app (Flask): The Flask application instance.
    users (dict): A dictionary containing user data with user IDs as keys.

Usage:
    Run this script to start the Flask development server. The application will be
    accessible at http://127.0.0.1:5000/ by default.
"""

app = Flask(__name__)

users = {
        1: {"name": "Ala", "age": 22},
        2: {"name": "Bartek", "age": 25},
        3: {"name": "Celina", "age": 30}
    }

@app.route('/hello', methods=['GET'])
def hello():
    return "Hello, World!"

@app.route('/user/<name>', methods=['GET'])
def greet_user(name):
    return f"Hello, {name}!"

@app.route('/', methods=['GET'])
def home():
    response = "<h1>Witamy na stronie głównej!</h1>"
    response += "<ul>"
    response += '<li><a href="/about">O nas</a></li>'
    response += '<li><a href="/users">Lista użytkowników</a></li>'
    response += "</ul>"
    return response


@app.route('/about', methods=['GET'])
def about():
    return "Strona o nas zawiera informacje o naszej aplikacji i jej twórcach."

@app.route('/users', methods=['GET'])
def get_users():
    user_links = {user_id: {"name": user["name"], "link": f"/user/{user_id}"} for user_id, user in users.items()}
    response = "<ul>"
    for user_id, user in user_links.items():
        response += f'<li><a href="{user["link"]}">{user["name"]}</a></li>'
    response += "</ul>"
    return response

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return f"{user['name']}, {user['age']} lat!"
    else:
        return f"Użytkownik nie istnieje!"

if __name__ == '__main__':
    app.run(debug=True)
