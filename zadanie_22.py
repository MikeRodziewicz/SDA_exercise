# Ćwiczenie 10.
# Napisz program "parzyste2.py", który wczyta od użytkownika liczbę całkowitą i
# bez użycia instrukcji "if" wyświetli informację, czy jest to liczba parzysta,
# czy nieparzysta.


n_type = ("even", "odd")
n = int(input("ender number: "))
print(n_type[n % 2])
