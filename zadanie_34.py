# Ćwiczenia 25.
# Napisz program, który wczyta od użytkownika liczbę X,
# a następnie wyświetli TRÓJKĄT prostokątny o długości przyprostokątnej X,
#  np.: 5 ->
# *
# * *
# *   *
# *     *
# *****"


liczba = int(input("dajez numer ziomek: "))


for row in range(liczba):
    for column in range(liczba):
        if column == 0 or row == (liczba-1) or row == column:
            print("*", end="")
        else:
            print(end=" ")
    print()
