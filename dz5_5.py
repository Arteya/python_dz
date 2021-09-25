src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
a = set()
result = []
for number in src:
    if (number in a) and (number in result):
        result.remove(number)
    else:
        result.append(number)
        a.add(number)
print(result)

