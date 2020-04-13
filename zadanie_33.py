# "Ćwiczenia 24.
# Napisz program, który wczyta od użytkownika tekst, a następnie wyświetli go w ramce z gwiazdek,
#  np.: HELLO STRANGER! ->
# *******************
# *   HELLO STRANGER!  *
# *******************"


def fun_print(t):
    print("*****************\n* {} * \n**************".format(t))


if __name__ == "__main__":
    user = input("zapodaj jakis tekst: ")
    fun_print(user)
