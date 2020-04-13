# 3. Napisz funkcję sum_up, która przyjmuje liczbę number.


def sum_up(a):
    b = 0
    for i in range(a):
        i = i+1
        b = b + i
    return b


if __name__ == '__main__':
    licz1 = int(input("podaj liczbe "))
    print(sum_up(licz1))
