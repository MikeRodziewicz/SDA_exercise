# •Wypisz 10 razy swoje imię na ekranie.


def name_display(n):
    print(n*10)


if __name__ == "__main__":
    name = input("podaj swoje imie ")
    name_display("{}\n".format(name))
