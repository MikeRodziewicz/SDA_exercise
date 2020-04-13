# "Ćwiczenia 26.
# Napisz program, który wczyta od użytkownika liczbę X, a następnie wyświetli romb o wysokości 2X,
#  np.: 2 ->
#
#   /\
#  /  \
#  \  /
#   \/
#
#
liczba = int(input("dajez numer ziomek: "))


def piramida(rows):
    # rows = rows*2
    for i in range(rows):
        print(" "*(rows-i-1)+"/" + " "*(i*2) + "\ ")
    for j in range(rows, 0, -1):
        print(" "*(rows-j) + "\\" + " "*((j-1)*2) + '/')
        # print(j-1)


piramida(liczba)
