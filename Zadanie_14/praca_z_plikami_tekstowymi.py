from backend import *


# po wejsciu w kazde zadanie pokazuje sie tresc zadania pobrana z pliku txt
#
# na samym dole pod trescia zadania pokazuja sie 2 opcje
# 1. Wyjscie
# 2. Pokaz wynik
#
# Pokaz wynik wyswietla zawartosc pliku z zadaniem
# Plik z zadaniem powinien byc umieszczony w folderze wraz z plikiem tekstowym
# zawierajacym jego tresc
#
# ** przycis Pokaz wynik powinien byc widoczny tylko wtedy jak istniej plik z rozwiazaniem.
# mozemy przyjac nazwe pliku taka jak TYTUL.py TYTUL.txt
# tytul to moga byc nazwy malymi literami odseparowane _ np zad_dodaj_1
# mozna przyjac dowolna formule wg wygody
#
# *** Dodatkowo mozna dodac do menu opcje 4. Dodaj nowe zadanie
# Dodawanie zadania powinno byc realizowane poprzez wybranie kategorii nastepnie
# podanie tresci(pobranej z inputa)
# na koncu wyswietleniu informacji o tym ze trzeba dostarczyc plik z rozwiazaniem

menu = ("1. Zadania proste", "2. Zadania srednie", "3. Zadania Trudne")


def selection(menu):
    for i in menu:
        print(i)


if __name__ == "__main__":
    selection(menu)
    wybor_kategorii = int(input("jakie zadanie chcesz wybrac? "))
    opening_file(wybor_kategorii)
    co_chcesz_zrobic()
    wybor_opcji = int(input("co chcesz zrobic? "))
    dalsze_czytanie(wybor_opcji)
