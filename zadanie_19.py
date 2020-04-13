# Ćwiczenie 19.
# Napisz program "powiel.py", który wczyta od użytkownika pewien napis,
# a następnie wyświetli 50 kopii tego napisu, każda w osobnej linii.

zdanie = input("napisz co chcesz ")


def powielanie(a):
    for x in range(51):
        print("\n{}".format(a))


powielanie(zdanie)
