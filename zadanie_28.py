# "Ćwiczenie 19.
# Zdefiniuj funkcję ""sylaby"", która dla parametru będącego wyrazem w języku polskim,
# zwróci listę jego sylab. Funkcja nie musi działać perfekcyjnie dla każdego wyrazu
#  (wyjątków itp.), ale im więcej przypadków obsłuży prawidłowo, tym lepiej."


# abrakadabra

samogloski = ('a', 'e', 'i', 'y', 'o', 'u')
wyjatki = ("ch", "rz", "sz", "dz")
inne = ("ą", "ę", "ć", "ś", "ż", "ź", "ń", "ó")


def sylaby(a):
    sylaba = ""
    sylaby = []
    for i in a:
        if i in samogloski:
            sylaba += i
            sylaby.append(sylaba)
            sylaba = ""
        else:
            sylaba += i
    if sylaba:
        sylaby[-1] = sylaby[-1] + sylaba

    print(",".join(sylaby))


if __name__ == "__main__":
    slowo = input("podaj slowo: ")
    sylaby(slowo)
