from random import seed
from random import randint

game = True
guess_count = 0
# liczba = randint(0, 1001)


def guess_number(a, b):
    global game
    secret_num = liczba
    global guess_count
    if a > secret_num:
        guess_count = guess_count + 1
        print("too high")
    elif a < secret_num:
        guess_count = guess_count + 1
        print("too low")
    elif a == secret_num:
        print(f"You have quessed with {guess_count} tries")
        game = False
    return guess_count


if __name__ == "__main__":
    liczba = randint(0, 1001)
    print(liczba)
    while game:
        try:
            user_quess = int(input("podaj liczbe: "))
            guess_number(user_quess, liczba)
        except:
            print("nie wprowdziles numeru: ")
