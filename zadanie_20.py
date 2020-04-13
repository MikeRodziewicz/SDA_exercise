# Ćwiczenie 6.
# Napisz program "pole_tr.py", który obliczy pole trójkąta,
# pod warunkiem że użytkownik poda wysokość i długość podstawy tego trójkąta.


a = int(input("podaj dlugosc boku"))
b = int(input("podaj wysokosc"))


def pole_tr(a, b):
    c = (a/2)*b
    print(c)


pole_tr(a, b)
