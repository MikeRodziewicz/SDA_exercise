# 2. Napisz funkcję divisible, która przyjmuje liczbę number oraz dzielnik
# divisor. Jej zadaniem jest sprawdzenie, czy liczba jest podzielna przez dzielnik.
#  Wykorzystaj w tym celu dzielenie modulo %. Jeżeli liczba jest podzielna przez
#  dzielnik, funkcja powinna zwrócić wartość True, jeżeli nie jest - wartość False.


def liczenie(a, b):
    if (a % b) == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    licz1 = int(input("podaj liczbe "))
    licz2 = int(input("podaj druga liczbe"))
#     print(liczenie(licz1, licz2))
