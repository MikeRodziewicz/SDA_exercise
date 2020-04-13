# "Ćwiczenie 21.
# Napisz program „lista.py”, który:
# a) Jeżeli na dysku nie ma pliku „lista.txt”, wczyta od użytkownika listę studentów
#  (imię, nazwisko, grupa) i zapisze ją do pliku „lista.txt”
# b) Jeżeli na dysku jest już plik „lista.txt”, wczyta z niego listę studentów
# (imię, nazwisko, grupa), a użytkownikowi umożliwi dopisywanie nowych studentów do listy,
# na koniec zapisze listę z powrotem do pliku."


def lista():
    edit = True
    x = path.exists("lista_studentow.txt")
    if x:
        while edit:
            f = open("lista_studentow.txt", "a")
            user_data = input("dodaj studentow")
            f.write(user_data)
            f.close
            edit = False
    else:
        print("does not exist")
        print("tworze plik")
        f = open("lista_studentow.txt", "w")
        f.write("\n")
        user_data = input("dodaj studentow")
        f.write(user_data)
        f.close
    f = open("lista_studentow.txt", "r")
    for i in f:
        print(i)
    f.close()


if __name__ == "__main__":
    lista()
