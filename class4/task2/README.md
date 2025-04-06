### Zadanie 2: Aplikacja To-Do - wersja Python lub JavaScript

Zbuduj prostą aplikację To-Do, która pozwala użytkownikowi:

- Dodawać nowe zadania
- Oznaczać zadania jako wykonane
- Usuwać zadania z listy

#### Wymagane trasy:
1. / – strona główna z linkami do:
2. /tasks – strona z listą zadań
3. /about – strona „O aplikacji”

#### Dwa podejścia do realizacji:

##### Podejście 1: Logika po stronie Pythona (Flask)

- Lista zadań przechowywana w zmiennej w Pythonie
- Dodawanie przez formularz HTML (metoda POST)
- Usuwanie i oznaczanie jako wykonane przez przekierowania (/delete/\<id>, /done/\<id>)
- Widoki renderowane przez Flask (render_template z Jinja2)

Użyjesz: request.form, redirect, url_for, @app.route


##### Podejście 2: Logika po stronie JavaScript (frontend)

- Lista zadań przechowywana w localStorage lub w zmiennej JS
- Wszystko dzieje się w przeglądarce (dodawanie, usuwanie, oznaczanie)
- Flask tylko dostarcza statyczne pliki i szablon HTML
- Stylizacja i interakcje w pełni w CSS + JS

Użyjesz: addEventListener, createElement, localStorage, fetch (opcjonalnie)
