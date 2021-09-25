def odd_num(number):
    return (num for num in range(1, number, 2))


odd_to_5 = odd_num(5)
print(next(odd_to_5))
print(next(odd_to_5))
print(next(odd_to_5))
print(next(odd_to_5))
