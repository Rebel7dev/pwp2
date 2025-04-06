### Zadanie 1: Mini portal z profilami (routing statyczny + dynamiczny)

Zbuduj prostą aplikację we Flasku z kilkoma stronami:

#### Wymagane ścieżki:
- / – strona główna z powitaniem i linkami do innych podstron
- /about – krótki opis „O nas”
- /users – lista użytkowników (dane zapisane w słowniku)
- /user/\<int:user_id> – profil konkretnego użytkownika (dynamiczny routing)

#### Dane przykładowe:

    users = {
        1: {"name": "Ala", "age": 22},
        2: {"name": "Bartek", "age": 25},
        3: {"name": "Celina", "age": 30}
    }

#### Przykład:
- /users → wyświetla listę imion z linkami do profili
- /user/2 → pokazuje „Bartek, 25 lat”
- /user/99 → „Użytkownik nie istnieje”
