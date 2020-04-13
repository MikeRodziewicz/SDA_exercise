# 5. Napisz funkcję leap_years, która przyjmuje parametr n i wyświetli n najbliższych lat przestępnych.
# Zdefiniuj w tym celu funkcję is_leap, która zwróci wartość True gdy rok jest przestępny
# (podzielny przez 4 i niepodzielny przez 100, lub podzielny przez 400: https://pl.wikipedia.org/wiki/Rok_przest%C4%99pny), a następnie wykorzystaj pętlę while.


def is_leap(year):
    if ((year % 4) == 0 and (year / 100) != 0) or (year / 400) == 0:
        return True
    else:
        return False


def leap_years(n):
    current_years = 0
    start_year = 2020
    while current_years < n:
        if (is_leap(start_year)):
            current_years += 1
            print(start_year)
        start_year += 1


if __name__ == '__main__':
    licz1 = int(input("podaj liczbe "))
    print(leap_years(licz1))
