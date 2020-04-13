# "Ćwiczenia 29.
# Napisz program, który wczyta od użytkownika tekst, a następnie podwoi w nim co drugi znak i wyświetli wynik,
#  np.: ALA MA PSA -> ALLA  MAA PPSAA"


def slowotok(a):
    nowa_lista = []
    counter = 0
    wynik = []
    separator = ""
    for i in a:
        nowa_lista.append(i)
    for j in nowa_lista:
        if counter % 2 == 0:
            wynik.append(j*2)
            counter += 1
        else:
            wynik.append(j)
            counter += 1
    print(separator.join(wynik))
    # print(nowa_lista)
    # print(wynik)


if __name__ == "__main__":
    liczba = input("dajez numer ziomek: ")
    slowotok(liczba)
