def odd_num(num):
    for number in range(1, num, 2):
        yield number


odd_to_5 = odd_num(5)
print(next(odd_to_5))
print(next(odd_to_5))
print(next(odd_to_5))
print(next(odd_to_5))
