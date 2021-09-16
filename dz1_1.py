duration = int(input('Введите секунды: '))
minute = duration // 60
hour = minute // 60
day = hour // 24
duration %= 60
minute %= 60
hour %= 24
print(f"{day}дн {hour}час {minute}мин {duration}сек")
