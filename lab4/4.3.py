n = int(input("Введите число городов: "))
cities = set()
for i in range(n):
    city = input("Введите название города: ").strip().lower()
    if city in cities:
        print("REPEAT")
    else:
        cities.add(city)
        print("OK")