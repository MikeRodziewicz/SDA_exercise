Ćwiczenia 27.
# Napisz program, który wczyta od użytkownika liczbę X, a następnie wyświetli kwadrat z gwiazdek o długości boku X,
#
#   np.: 4 ->
# ****
# *    *
# *    *
# ****"
liczba = int(input("dajez numer ziomek: "))


def kwadrat(rows):
    for i in range(rows):
        if (i == 0 or i == rows-1):
            print("* "*(rows))
        else:
            print("* " + "  "*(rows-2)+"*")


kwadrat(liczba)
