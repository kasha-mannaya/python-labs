symbols = ',.!?:;"()\t\n'
data = input("Введите текст: ")
for sym in symbols:
    data = data.replace(sym, '')
data = data.split()
print('The asnwer is:\n' +'\n'.join(sorted(sorted(set(data)), key=lambda word: data.count(word), reverse=True)))