# (przykladowa tablica
# [3, 6, 12, 333, 1, 988, 22121, 4, 22]
# [0, 1, 2, 3, 4, 5, 6]
# [11, 10, 9, 8, 7, 6, 5, 4, 3, 2 ,1, 0]
# )
#
# Tablice 1. Napisz metodę print, która wypisze w konsoli elementy tablicy intów, przekazanej jako parametr.
# 2. Napisz metodę getMax, która przyjmie za parametr tablicę intów, a która zwróci największą wartość z tej tablicy.
# 3. Napisz metodę getMin, która zwróci najmniejszy element przekazanej tablicy intów.
# 4. Napisz metodę getSum, która przyjmie za parametr tablicę intów, a któa zwróci sumę jej elementów.
# 5. Napisz metodę getMaxMinAndSum, która przyjmie za parametr tablicę intów, a która zwróci tablicę trzyelementową, której pierwszy element to wartość największa, drugi to najmniejsza, a trzeci suma wszystkich elementów.
# 6. Napisz metodę getLarger, która przyjmie za parametry dwie tablice intów, a która zwróci tę tablicę, której suma elementów jest większa.
# 7. Napisz metodę merge, która za parametry dwie tablice intów, a która zwróci tablicę, która zawierać będzie wszystkie elementy z jednej i drugiej tablicy.


# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
#
# for x in list2:
#     list1.append(x)


przykladowa = ([3, 6, 12, 333, 1, 988, 22121, 4, 22], [0, 1, 2, 3, 4, 5, 6],
               [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

przykladowa1 = ([3, 5, 12, 333, 1, 988, 22121, 4, 22], [1000, 1, 2, 3, 4, 5, 6],
                [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

# lista1 = przykladowa[0]
# lista2 = przykladowa[1]
# lista3 = przykladowa[2]


def pokaz(a):
    lista1 = a[0]
    lista2 = a[1]
    lista3 = a[2]


def getMax(a):
    lista1 = a[0]
    lista2 = a[1]
    lista3 = a[2]
    suma = lista1+lista2+lista3
    return max(suma)


def getMin(a):
    lista1 = a[0]
    lista2 = a[1]
    lista3 = a[2]
    suma = lista1+lista2+lista3
    return min(suma)


def getSum(a):
    lista1 = a[0]
    lista2 = a[1]
    lista3 = a[2]
    suma = lista1+lista2+lista3
    return sum(suma)


def getMaxMinAndSum(a):
    lista1 = a[0]
    lista2 = a[1]
    lista3 = a[2]
    nowa_lista = [getMax(a), getMin(a), getSum(a)]
    return nowa_lista


def getLarger(a, b):
    new_list_a = []
    new_list_b = []
    for item in a:
        new_list_a += item
    for item in b:
        new_list_b += item
    if sum(new_list_a) > sum(new_list_b):
        return "pierwsza tablica jest wieksza, wynosi {}".format(sum(new_list_a))
    else:
        return "druga tablica jest wieksza, wynosi {}".format(sum(new_list_b))


def merge_tables(a, b):
    new_list_a = []
    new_list_b = []
    wynik = []
    for item in a:
        new_list_a += item
    for item in b:
        new_list_b += item
    wynik = new_list_a + new_list_b
    return wynik


print(merge_tables(przykladowa, przykladowa1))
