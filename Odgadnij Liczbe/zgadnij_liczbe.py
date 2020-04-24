# import random to generate number, seed probably not needed, attrgetter imported to
# use sorted method with the class objects
from random import seed
from random import randint
from operator import attrgetter

# double while loops so two game statuses.
game = True
master_game = True
guess_count = 1
wybor_poziomu = 0
menu_choice = 0
user_name = ''
user_level = ''
menu = ["1. Graj", "2. Pokaz Ranking", "3. Wyjscie"]
diff = ["1. łatwy", "2. Średni", "3. Trudny"]

# generate class based on the input from users to allow for ranking sort


class Zawodnik():
    def __init__(self, name, poziom, score):
        self.name = name
        self.poziom = poziom
        self.score = score

    def __repr__(self):
        # format of the final print
        return "{} gral na poziomie {} i zgadl po {} probach \n".format(self.name, self.poziom, self.score)

# menu - has to return int for menu choice


def show_menu(a):
    global menu_choice
    print("Menu: ")
    for i in a:
        print(i)
    try:
        menu_choice = int(input("wybierz opcje z menu: "))
        return menu_choice
    except:
        print("nie wprowdziles numeru: ")
        show_menu(a)

# starts when correct manu selection happens


def wybierz_poziom(a):
    global wybor_poziomu
    print("Poziomy Trudności: ")
    for i in a:
        print(i)
    try:
        wybor_poziomu = int(input("wybierz poziom trudnosci: "))
        return wybor_poziomu
    except:
        print("nie wprowdziles numeru: ")
        wybierz_poziom(a)

# based on the wybierz_poziom selection generates number in the correct range.
# also returns string representation for the difficulty level


def poziomy_trudnosci(a):
    global secret_number
    global diff
    global user_level
    if a == 1:
        secret_number = randint(0, 10)
        user_level = "Łatwy"
    elif a == 2:
        secret_number = randint(0, 100)
        user_level = "Średni"
    elif a == 3:
        secret_number = randint(0, 1000)
        user_level = "Trudny"
    return secret_number
    return user_level

# writes and saves the file with the data separated by # signs to later split them
# resets the quess count to 1 so that next player does not add but starts from 1


def zapisz_wynik(a, b, c):
    global guess_count
    with open("ranking.txt", 'a+') as f:
        f.write(f"{a}#{b}#{c}\n")
        f.close()
    guess_count = 1

# checks the number inside the second loop, when win - stops the second (inner) loop


def guess_number(a, b):
    global game
    global guess_count
    global user_name
    global user_level
    if a > b:
        guess_count = guess_count + 1
        print("too high")
    elif a < b:
        guess_count = guess_count + 1
        print("too low")
    elif a == b:
        print(f"{user_name}, grales na poziomie trudnosci {user_level}, zgadles liczbe po {guess_count} probach")
        game = False

# open the file, reads lines, makes each line into object in a list
# breaks down each line based on the #, each part is put ino a new list where it can be access by index guess_number
# takes these three items and passes them to the Zawodnik class, to create class object
# uses attrgetter method (imported at the start) to sort the class objects based on the class object atrribute "score"
# prints objects using Zawodnik class str method


def pokaz_ranking():
    ranking = []
    lista_zawodnikow = []
    file = open("ranking.txt", 'r')
    linijki = file.readlines()
    for i in linijki:
        i = i.strip().split('#')
        ranking.append(i)
    file.close()
    for i in ranking:
        lista_zawodnikow.append(Zawodnik(i[0], i[1], int(i[2])))
    sorted_lista_zawodnikow = sorted(lista_zawodnikow, key=attrgetter('score'))
    for i in sorted_lista_zawodnikow:
        print(i)


if __name__ == "__main__":
    while master_game:
        show_menu(menu)
        if menu_choice == 1:
            game = True
            user_name = input("podaj swoje imie: ")
            wybierz_poziom(diff)
            poziomy_trudnosci(wybor_poziomu)
            while game:
                try:
                    user_quess = int(input("podaj liczbe: "))
                    guess_number(user_quess, secret_number)
                except:
                    print("nie podales numeru")
            zapisz_wynik(user_name, user_level, guess_count)
        elif menu_choice == 2:
            try:
                pokaz_ranking()
            except:
                print("nie ma jeszcze ranki")
        elif menu_choice == 3:
            break
