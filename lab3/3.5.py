def determinant(a):
    return a[0][0] * a[1][1] * a[2][2] + a[0][2] * a[1][0] * a[2][1] + a[0][1] * a[1][2] * a[2][0] - \
        a[0][2] * a[1][1] * a[2][0] - a[0][1] * a[1][0] * a[2][2] - a[0][0] * a[1][2] * a[2][1]

n = int(input("Введите размер матрицы: "))
print("Введите матрицу:")
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
    assert len(a[-1]) == n
if determinant(a):
    print("Столбцы матрицы линейно независимы.")
else:
    print("Столбцы матрицы линейно зависимы.")
for i in range(len(a)):
    for j in range(len(a)):
        a[i][j] = str(a[i][j])
for i in a:
    print("\t".join(i))