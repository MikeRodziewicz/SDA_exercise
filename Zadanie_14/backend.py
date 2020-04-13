def opening_file(a):
    f = open('zadania.txt', 'r')
    lines = list(f)
    if a == 1:
        for x in lines[0:3]:
            print(x, end='')
    elif a == 2:
        for x in lines[3:6]:
            print(x, end='')
    elif a == 3:
        for x in lines[6:9]:
            print(x, end='')
    f.close()


def co_chcesz_zrobic():
    global wybor_opcji
    menu = ("1. Pokaz wynik", "2. Wyjscie")
    for x in menu:
        print(x)


def dalsze_czytanie(a):
    if a == 1:
        f = open('zadania_latwe.txt', 'r')
        print(f.read())
        f.close()
    elif a == 2:
        f = open('zadania_srednie.txt', 'r')
        print(f.read())
        f.close()
