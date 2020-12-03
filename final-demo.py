import csv
f = open('populationbyage.csv')
data = csv.reader(f)
next(data); next(data)

result = []
total10 = [];total20 = [];total30 = [];total40 = [];total50 = [];total60 = []

for row in data:
    row[1:] = map(int, row[1:])
    if '15 - 19세' in row[0]:
        for i in range(4):
            a = row[i * 5 + 3]
            print(a)
    elif '20 - 29세' in row[0]:
        for i in range(4):
            b = row[i * 5 + 3]
            print(b)
    elif '30 - 39세' in row[0]:
        for i in range(4):
            c = row[i * 5 + 3]
            print(c)
    elif '40 - 49세' in row[0]:
        for i in range(4):
            d = row[i * 5 + 3]
            print(d)
    elif '50 - 59세' in row[0]:
        for i in range(4):
            e = row[i * 5 + 3]
            print(e)
    elif '60세이상' in row[0]:
        for i in range(4):
            f = row[i * 5 + 3]
            print(f)
        for i in range(4,7):
            f2 = row[i * 5 + 3]
            print(f2)
            
    