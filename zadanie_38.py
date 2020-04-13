# "Ćwiczenia 30.
# Napisz program, który wczyta od użytkownika tekst, a następnie wyświetli go w dwóch linijkach naprzemiennie,
# np.: HELLO STRANGER! ->
# H L O S R N E !
# E L   T A G R"


def odwracacz(zdanie):
    print(zdanie[::2])
    print(zdanie[1::2])


if __name__ == "__main__":
    zdanie = input("podaj zadanie: ")
    odwracacz(zdanie)
