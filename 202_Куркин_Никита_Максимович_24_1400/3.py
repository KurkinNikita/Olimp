a = open("transactions.csv")

p = []
m = a.read()# читаю файл
n = []
n = n.append(m)# добавляю в массив

k = int(input('Введите номер транзакции: '))
while True:
    for i in range(len(n)-1):
        if n[i+1] == k:
            o = 'По вашему запросу: ' + str(k) + 'найден следующий вариант' + str(n[i] + n[i+1] + n[i+2] + n[i+3] + n[i+4] + n[i+5] + n[i+6])
        else:
            o = False
    return o

print(o)