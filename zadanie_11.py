# zad 11
# # Write function that takes two args: list of strings and a prefix (string).
# # The function should iterate over the list and find all strings which start with the prefix, then return list of such strings
#
# thislist = ["apple", "banana", "cherry", 'apeddd', 'apeeeddd', 'apddd', 'sapeddd']


thislist = ["apple", "banana", "cherry", 'apeddd', 'apeeeddd', 'apddd', 'sapeddd']


def iteration_prefix(a, b):
    results = []
    for i in a:
        if i.startswith(b):
            results.append(i)
    return results


print(iteration_prefix(thislist, "ap"))
