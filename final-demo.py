import csv
f = open('populationbyage.csv')
data = csv.reader(f)
next(data); next(data)

result = []
total10 = [];total20 = [];total30 = [];total40 = [];total50 = [];total60 = []

'''
for row in data:
    row[4:5] = map(int, row[4:5])
    result.append(row[3])
 

print(result)
''' 

for row in data:
    row[1:] = map(int, row[1:])
    for i in range(6):
        a = row[i * 5 + 3]
    print(a)