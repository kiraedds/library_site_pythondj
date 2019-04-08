# TEMAT: APLIKACJA DO ZARZĄDZANIA BIBLIOTEKĄ

# STORY:
## 1. Logowanie do systemu. Różne role i uzależnione od tego widoki;
Widok: bibliotekarza/bibliotekarki, wypożyczający, księgowa, kierownik;

## 2. Dodawanie nowych książek oraz edycja istniejących w bazie biblioteki;
Panel wyświetlający informacje o danej książce, historii wypożyczeń;
Uprawnienia dostępu: bibliotekarz/bibliotekarka, logistyka

## 3. Dodawanie i edycja użytkowników do bazy biblioteki.
Wyszukiwarka po imieniu, nazwisku, numerze karty bibliotecznej oraz panel wyświetlający dane użytkownika wraz z harmonogramem jego wypożyczeń.
Uprawnienia dostępu: bibliotekarz/bibliotekarka;

## 4. Ustalanie terminu wypożyczania książki przez użytkownika wraz z terminem oddania.
Możliwość wyszukiwania książek po typie, tytule, autorze. Informacja na temat dostępności książki.
Uprawnienia: wypożyczający, bibliotekarz/bibliotekarka

## 5. Wyszukiwarka wypożyczonych książek wraz z terminami oddania, naliczonymi kosztami oraz dostępnością wybranych tytułów.
Widok ogólny, pozwalający wyświetlić wielu użytkowników.
Uprawnienia: bibliotekarz/bibliotekarka

## 6. Panel harmonogramu pracy bibliotekarza/ bibliotekarki na najbliższy tydzień, miesiąc, rok.
Widok kalendarza z możliwością edycji w trybie kierownika. Po naciśnięciu na dany dzień widać szczegóły dnia.
Uprawnienia: kierownik.

## 7. Historia zmian w programie - wszystkie zmiany zapisywane w bazie danych.
Panel wyświetlania zmian. Wyszukiwarka po dacie, trybie zmiany (dodawanie, edycja) oraz prawach dostępu np. wyszukaj wszystkie nowe książki wprowadzone wczoraj.
Uprawnienia: kierownik.

## 8. Panel księgowej. Uprawnienia: kierownik (tryb odczytu) i księgowa tryb edycji.
Wyszukiwarka zakupionych książek po: cenie, dacie dodania oraz wyświetlanie zamówień (wiele książek): cena, ilość książek, opłacone lub nieopłacone.

Aktorzy:
Książka: tytuł, autor, ISBN, gatunek, wydawnictwo, rok wydania;
Bibliotekarz/Bibliotekarka: imię, nazwisko, wiek, płeć, kalendarz pracy;
Wypożyczający: imię, nazwisko, numer identyfikacji, PESEL
Kierownik: imię, nazwisko, ile lat doświadczenia, ile lat w firmie, kalendarz pracy;
Księgowa: imię, nazwisko, ile lat doświadczenia, ile lat w firmie;

# PyCharm + Python;

# Instalacja Django;

# Ważne;

Podczas instalacji Django należy narzucić wersję 1.8.6, wersje wyższe mogą powodować dziwne błędy;
Aby tego dokonać: pip install Django==1.8.6

## Windows
0) Uruchom PowerShell w trybie administratora.
1) Sprawdź czy masz zainstalowanego Pythona. Komenda "py --version" powinna zadziałać. Jeśli nie, zainstaluj Pythona.
2) Spróbuj wpisać "easy_install --version", jeśli nie działa, to prawdopodobnie posiadasz to narzędzie, ale należy je skonfigurować.
2a) Wejdź do katalogu, w którym masz zainstalowanego Pythona, np. "C:\Python_3.7.0-32bit", dalej "Scripts", powinien tam być plik .exe "easy_install.exe".
2b) "easy_install.exe" -> PPM -> Właściwośći. Skopiuj "Lokalizacja".
2c) Dalej patrz : https://youtu.be/qgGIqRFvFFk -> PyCharm + Django tutorial.

# Uruchamianie projektu z repozytorium;

1) Otworzyć Projekt_Django w PyCharm;
2) W terminalu PyCharm wpisać:
-> cd django_biblioteka
-> cd library_app
-> (opcjonalnie) python manage.py createsuperuser        (tworzenie swojego profilu superusera w bazie danych)
-> python manage.py makemigrations biblioteka
-> python manage.py migrate
-> python manage.py runserver
-> Aby przerwać działanie serwera wystarczy w terminalu PyCharm wcisnąć "Ctrl+C";
3) Adres serwera: http://127.0.0.1:8000/admin/   LUB   http://127.0.0.1:8000/biblioteka/
4) w /admin można dodawać książki, autorów, itd;

# models.py modele (tabele bazy danych)
# szablony (html) templates/biblioteka/book