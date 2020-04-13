# Ćwiczenie 4.
# Napisz skrypt, który zsumuje dwie liczby, nie używając znaku "+" (w całym skrypcie)


def add_no_sign(a, b):
    c = []
    c.append(a)
    c.append(b)
    return(sum(c))


print(add_no_sign(3, 4))
