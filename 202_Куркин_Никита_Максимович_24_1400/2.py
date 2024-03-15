a = open("transactions.csv")

p = []
m = a.read()# читаю файл
n = []
n = n.append(m)# добавляю в массив

def sorted(h):
    for i in range(len(h) - 1):
        if h[i] > h[i+1]:
            return h.reverse(h[i+1], h[i])
        else:
            return str(h[i], h[i+1])
print(h)