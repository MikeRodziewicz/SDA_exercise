# "Ćwiczenie 22.
# Wykorzystując funkcję sylaby z ćwiczenia III z lekcji 8,
# napisz program „sylab.py”, który wczyta plik tekstowy o podanej przez
# użytkownika nazwie i rozbije zawarty w nim tekst na sylaby."


samogloski = ('a', 'e', 'i', 'y', 'o', 'u')
wyjatki = ("ch", "rz", "sz", "dz")
inne = ("ą", "ę", "ć", "ś", "ż", "ź", "ń", "ó")


def user_file(a):
    x = f"{a}.txt"
    y = open(f"{x}", 'r')
    print(y.read())


def sylaby(a):
    x = f"{a}.txt"
    y = open(f"{x}", 'r')
    sylaba = ""
    sylaby = []
    for i in y:
        for y in i:
            if y in samogloski:
                sylaba += y
                sylaby.append(sylaba)
                sylaba = ""
            else:
                sylaba += y
        # if sylaba:
        #     sylaby[-1] = sylaby[-1] + sylaba
        print(sylaby)


if __name__ == "__main__":
    file_by_user = input("podaj nazwe dokumentu: ")
    sylaby(file_by_user)
