# "3. Napisz funkcję reverse_list, która przyjmuje listę processed_list.
# Jej zadaniem jest obrócenie kolejności elementów w tej liście i zwrócenie odwróconej listy
#  (przykładowo, dla listy [1, 2, 3, 4], funkcja powinna zwrócić listę [4, 3, 2, 1]).
#  Uwaga: nie używaj wbudowanej funkcji reversed ani metody .reversed.
# -- inna wersja tego zadania
# Kolejna misja, to odwracanie stringów (jakkolwiek miałoby to nie brzmieć ;)).
# Zakładamy, że mamy wejściowy string ""hello world"" i chcemy na wyjściu otrzymać ""dlrow olleh"".
#
# 3.1 Wykorzystując funkcję reverse_list, przygotuj funkcję is_palindrome,
# która przyjmować będzie tekst text. Funkcja ta ma sprawdzić, czy tekst jest palindromem,
# tzn. czy ma taką samą postać czytany od przodu i od tyłu (przykładem palindromu jest słowo ""kajak"").
# Upewnij się, że Twoja funkcja reverse_list działa również dla łańcuchów znaków (stringów)"

thislist = ["apple", "banana", "cherry", 'apeddd', 'apeeeddd', 'apddd', 'sapeddd']


def reverese(something):
    return something[::-1]


print(reverese(thislist))


def is_palindroe(cos):
    if str(cos) == str(cos)[::-1]:
        return True
    else:
        return False


print(is_palindroe("kajak"))
