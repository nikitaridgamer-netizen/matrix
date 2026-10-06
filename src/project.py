n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))
matritsa = []

for i in range(n):
    stroka = []
    for j in range(m):
        stroka.append(float(input("Введите элемент: ")))
    matritsa.append(stroka)

print("Исходная матрица:")

for stroka in matritsa:
    print(stroka)

k = int(input("Введите номер столбца для удаления: "))

while k < 1 or k > m:
    print("Такого столбца нет")
    k = int(input("Введите номер столбца для удаления: "))

for stroka in matritsa:
    stroka.pop(k - 1)

print("Матрица после удаления:")

for stroka in matritsa:
    print(stroka)

input("")