a = open('pack.txt')
p = []
m = a.read()# читаю файл
n = []
n = n.append(m)# добавляю в массив
for i in range(len(n) - 1):
    if n[i] == 'УПАКОВКА' or n[i+1] == "Упаковка" or n[i+2] == "упаковка":# поиск ключевого слова
        u = p.append([for j in n: n[j]])# вписываю наименование товара
print(u)