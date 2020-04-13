# Ćwiczenie 8.
# Napisz program "parzyste.py", który wczyta od użytkownika liczbę całkowitą i
# wyświetli informację, czy jest to liczba parzysta, czy nieparzysta.


liczba = int(input("podaj liczbe"))


def odd_even(a):
    if a % 2 == 0:
        print("parzyste")
    else:
        print("nieparzyste")


odd_even(liczba)
