# "Ćwiczenie 20.
# Napisz program ""login.py"", który wczyta od użytkownika login i hasło.
# Jeżeli w słowniku haseł znajduje się odpowiedni login i hasło, program powinien
# wyświetlić „Autoryzacja pomyślna” inaczej – „Błąd logowania”."


slownik = {"tomek2": "sosnowiec", "wojtas14": "bytom"}


def login(a, b):
    if a in slownik:
        if b in slownik.values():
            print("logowanie poprawne")
    else:
        print("podany login jest nieprawidlowy")


if __name__ == "__main__":
    podaj_login = input("podaj swoj login: ")
    podaj_haslo = input("podaj swoje haslo: ")
    login(podaj_login, podaj_haslo)
