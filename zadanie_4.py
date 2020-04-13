# 4. Napisz funkcję factorial, która zwracać będzie wartość silni zadanej wartości.
# Silnia (oznaczana jako n!), dla liczb całkowitych większych od 0 stanowi iloczyn
# tej liczby oraz wszystkich mniejszych liczb całkowitych
# (czyli 1! = 1, 2! = 2 * 1, 3! = 3 * 2 * 1 itd.), a dla 0 0! = 0. Wykorzystaj w tym celu pętlę while.


def silnia(a):
    b = 1
    for i in range(a):
        i = i+1
        b = b * i
    return b


if __name__ == '__main__':
    licz1 = int(input("podaj liczbe "))
    print(silnia(licz1))
