# 6. # Write function which takes string AAAAaaBCC CDDe as argument and returns its compressed version A4a2B1C3D2e1
# https://stackoverflow.com/questions/32855812/create-a-compress-function-in-python


def kompiler(slowo):
    results = ""
    count = 1

    results += slowo[0]

    for i in range(len(slowo)-1):
        if(slowo[i] == slowo[i+1]):
            count += 1
        else:
            if(count > 1):
                results += str(count)
            results += slowo[i+1]
            count = 1
    if(count > 1):
        results += str(count)
    return results


print(kompiler("aaaabbceig2222aaaa"))
