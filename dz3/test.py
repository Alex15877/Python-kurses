a = []
b = int(input("Введите начальное число: "))
n = int(input("Введите последние число: "))

if b >= n:
    print("Начальное число не может быть польше или равно последнему!")

    for i in range(3, n + 1, 2):
        k = 0
        q = int(n**0.5) + 2
        for j in a:
            if j > q:
                break
            if i % j == 0:
                k = 1
                break
        if k == 0:
            a.append(i)
print(a)
print(b,n)