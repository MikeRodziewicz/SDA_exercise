# "Ćwiczenie 18.
# Zdefiniuj funkcję ""avg"", która dla dowolnej liczby parametrów zwróci ich średnią
# arytmetyczną (lub 0 dla 0 parametrów)."


oceny = [1, 2, 3, 4]


def avarege(*args):
    if args == 0:
        print(0)
    else:
        b = sum(args) / len(args)
        print(b)


avarege(1, 2, 3, 8, 7)
