# Zad
# Masz liste ["Wyjscie", "Ddodaj", "Odejmij", "Pomnoz", "Podziel"]
# (nie dotyczy wartosci Wyjscie)
# 1 Stworz funkcje o takich samych nazwach jak w liscie,
# 2 kazda funkcja przyjmuje 2 parametry liczbowe i zwraca wynik ich dzialania
# 3 na podstawie listy stworz menu ktore bedzie wyswietlane na ekranie
# 4 po wyswietleniu Menu czekaj na akcje z konsoli i po wybraniu odpowiedniego numerka wykonaj czynnosc dla danej akcji
# 4.1 dla wyjscie wyjdz
# 4.2 dla innych funkcji - pobierz 2 wartosci z konsoli do zmiennych a i b
# 4.3 uruchom odpowiednia funkcje z pobranymi parametrami i wyswietl wynik
#
# Dodatkowe
# 5. do inputa mozna uzyc metody napisanej wczoraj get_input_int
# 6. zmien metode get_input_int w taki spsob ze przy wykorzystaniu while
#         zamiast zwracac blad powtorzy zapytanie o liczbe
# 7. przy wykorzystaniu petli while. po zakonczeniu dodawania wyswietl ponownie menu. Warunkiem zakonczenia jest wybranie opcji Wyjscie


my_list = ["Wyjscie", "Ddodaj", "Odejmij", "Pomnoz", "Podziel"]
game = True


def selection(opcje):
    for i in opcje:
        print(opcje.index(i)+1, i)


def kalkulacje(a, b, c):
    if a == 2:
        return b+c
    elif a == 3:
        return b-c
    elif a == 4:
        return b*c
    elif a == 5:
        return b/c


if __name__ == "__main__":
    selection(my_list)
    while game:
        try:
            wybor = int(input("wybierz opcje z listy "))
            if wybor == 1:
                print("byebye")
                game = False
            else:
                licz1 = int(input("podaj pierwsza liczbe "))
                licz2 = int(input("podaj druga liczbe "))
                print(kalkulacje(wybor, licz1, licz2))
        except:
            selection(my_list)
