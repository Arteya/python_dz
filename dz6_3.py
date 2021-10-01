from itertools import zip_longest  # я думала, что нельзя доп библ использовать. С зип_лонгестом все проще.
list_names = []
user = open('users.csv', 'r', encoding='utf-8')
for line in user:
    # print(line)
    list_names.append(line)
user.close()

list_hobbies = []
hobby = open('hobby.csv', 'r', encoding='utf-8')
for line in hobby:
    # print(line)
    list_hobbies.append(line)
hobby.close()
# print(len(list_names))
# print(len(list_hobbies))

if len(list_names) < len(list_hobbies):
    print(exit(1))
else:
    name_hobby = dict(zip_longest(list_names, list_hobbies))
    # print(name_hobby)
    with open("hobby_name.csv", "w", encoding='utf-8') as file:
        print(name_hobby, file=file)
c = open('hobby_name.csv', 'r', encoding='utf-8')
for line in c:
    print(line)
c.close()
