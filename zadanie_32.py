# # "Ćwiczenie 23.
# # Napisz program, który przeliczy wprowadzoną liczbę rzymską na jej postać dziesiętną."
#
cyfry_rzymskie = {"I": "1", "II": "2", "III": "3", "IV": "4", "V": "5",
                  "VI": "6", "VII": "7", "VIII": "8", "IX": "9", "X": "10"}


def cyfry(a):
    global cyfry_rzymskie
    nowa_liczba = []
    liczba_koncowa = []
    y = 0
    for i in a:
        if i in cyfry_rzymskie:
            nowa_liczba.append(i)
            # print(nowa_liczba)
    for i in nowa_liczba:
        liczba_koncowa.append(cyfry_rzymskie[i])
    print(liczba_koncowa)
    for i in liczba_koncowa:
        y = y + int(i)
    print(y)


cyfry("IX")

# prawidlowe rozwiazanie (nie jest moje)


def decode_roman_numeral(roman):
    """Calculate the numeric value of a Roman numeral (in capital letters)"""
    trans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    values = [trans[r] for r in roman]
    return sum(
        val if val >= next_val else -val
        for val, next_val in zip(values[:-1], values[1:])
    ) + values[-1]


print(decode_roman_numeral("IX"))
