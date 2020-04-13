# "Ćwiczenie 16.
# Napisz program ""wyrazy.py"", który wczyta od użytkownika pewien tekst,
# a następnie podzieli go na zdania (zakładamy, że jednoznacznie kropka rozdziela zdania)
#  i dla każdego zdania wyświetli ile jest w nim wyrazów (zakładamy, że spacja oddziela wyrazy w zdaniu)."

#
# foo = [['ale', 'ma', 'kota'], ['', 'tata', 'ma', 'psa']]
# print(len(foo[0])-1)
# for i in foo:
#     print(len(i))


def wyrazy(a):
    nowe = a.split(".")
    jeszcze_nowsze = []
    c = " "
    d = ''
    for i in nowe:
        jeszcze_nowsze.append(i.split(" "))

    for b in jeszcze_nowsze:
        print(b)
        print(len(b))


if __name__ == "__main__":
    user = input("napisz jakies zadnie: ")
    wyrazy(user)
