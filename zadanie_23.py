# "Ćwiczenie 11.
# Napisz program ""numer.py"", który zamieni wprowadzony przez użytkownika ciąg cyfr na formę tekstową:
# a) znaki nie będące cyframi mają być ignorowane
# b) konwertujemy cyfry, nie liczby, a zatem:
# - 911 to ""dziewięć jeden jeden""
# - 1100 to ""jeden jeden zero zero"""


dictio = {"1": "jeden", "2": "dwa"}
user_number = input("podaj numer: ")


def number_iteration(a):
    nowy_string = []
    try:
        for i in a:
            x = dictio.get(i)
            nowy_string.append(x)
            print(nowy_string)
    except:
        print("zly numer, musisz sprobowac raz jeszcze")


number_iteration(user_number)
