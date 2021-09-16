list_cube = []
list_cube_plus = []
all_sum = 0
for i in range(1, 1000, 2):
    list_cube.append(i ** 3)
for i, v in enumerate(list_cube):
    # print(v,'----')
    # print(list_cube[i])
    sum_num = 0
    while v > 0:
        sum_num += v % 10
        v //= 10
    if sum_num % 7 == 0:
        all_sum += list_cube[i]
print(all_sum)
#     while list_cube[i] > 0:
#         sum_num += list_cube[i] % 10 # почему наоборот, а результат одинаковй?
#         list_cube[i]//= 10
#     if sum_num % 7 == 0:
#         all_sum += v
# print(all_sum)
for n in list_cube:
    list_cube_plus.append(n + 17)
all_sum = 0
for i, v in enumerate(list_cube_plus):
    sum_num = 0
    while v > 0:
        sum_num += v % 10
        v //= 10
    if sum_num % 7 == 0:
        all_sum += list_cube_plus[i]
print(all_sum)
# sum = 0
# q = 0
# while q < len(list_cube):
#     q = q + 1                          # изначально пталась слепить химеру из двух циклов while. Это было бесполезно?
# while (list_cube[3] != 0):             # индекс 3 - это что бы посмотреть считает ли сумму цифр.
#     sum = sum + list_cube[3] % 10
#     list_cube[3] = list_cube[3] // 10
# print(sum)

