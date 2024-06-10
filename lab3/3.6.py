data = input("Введите: ").strip().split()
answer = ""
for elem in data:
    answer += elem[0].capitalize()
print(answer)