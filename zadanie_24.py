# "Ćwiczenie 13.
# Napisz program ""oceny.py"", który wczytuje od użytkownika kolejne oceny i:
# a) sprawdza czy wprowadzona ocena jest na liście dopuszczalnych na wydziale
# ocen (jeżeli ocena jest na liście dopuszczalnych na wydziale ocen, dodaje ją na listę otrzymanych ocen)
# b) jeżeli wciśnięto sam Enter, oznacza to koniec listy otrzymanych ocen
# c) wyświetla wyliczoną dla listy otrzymanych ocen średnią arytmetyczną."


game = True
dopuszczalne_liczby = (1, 2, 3, 4, 5, 6)
suma_ocen = []
srednia = 0


def sprawdzenie_i_srednia(a):
    a = int(a)
    if a in dopuszczalne_liczby:
        suma_ocen.append(a)
        srednia = sum(suma_ocen)/len(suma_ocen)
    return srednia


if __name__ == "__main__":
    while game:
        try:
            ocena = input("wprowadz swoja ocene: ")
            if ocena == "":
                print("koniec gry")
                break
            else:
                print(sprawdzenie_i_srednia(ocena))
        except:
            print("coś poszło nie tak...")
