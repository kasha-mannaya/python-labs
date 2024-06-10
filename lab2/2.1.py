def make_triangle(n):
    triangle = [[1]]
    for i in range(1,n):
        pre_str = triangle[-1]
        new_str = [1]
        for j in range(1,i):
            new_str.append(pre_str[j-1] + pre_str[j])
        new_str.append(1)
        triangle.append(new_str)
    return(triangle)
n = int(input("введитк количество строк: "))
pascal_triangle = make_triangle(n)
for stroka in pascal_triangle:
    print(*stroka)