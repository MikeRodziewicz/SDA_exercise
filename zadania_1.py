# 1. Napisz funkcję greet, która jako argument
# przyjmować będzie imię name oraz drukować będzie powitanie (np. greet('Piotrek')
# powinno wyświetlić w konsoli tekst w stylu 'Witaj, Piotrek!). Przetestuj działanie
# programu w bloku if __name__ == '__main__'. Dodatkowo, spróbuj rozszerzyć funkcję
# w taki sposób, by wyświetlała specjalny tekst wówczas,
# gdy podasz swoje imię (czyli np. Witaj, Piotrek, ładna dziś pogoda!, ale dla innych imion Cześć, Agata!).


from os import path
import os
import random


def greet(name):
    moje_imie = "michal"
    if name == moje_imie:
        return "witaj{}".format(moje_imie)
    else:
        return "czego tu szukasz {}".format(name)


if __name__ == '__main__':
    odp = input("puk puk, kto tam? ")
    print(greet(odp))
