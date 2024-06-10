data = {}
inp = input("Введите текст: ").replace(',.!?:;"()\t\n', '').split()
answer = ''
for word in inp:
    if not word in data.keys():
        data[word] = -1
    data[word] += 1
    answer += str(data[word]) + ' '
print(answer)