log = open('nginx_logs.txt', 'r', encoding='utf-8')
# for line in log:
#     content = (line.split()[0], line.split()[5][1:], line.split()[6])
#     print(type(content))
# log.close()

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    content = ((line.split()[0], line.split()[5][1:], line.split()[6]) for line in f)  # этот вариант круче потому, что генератор?
    print(type(content))
    for i in content:
        print(type(i))
