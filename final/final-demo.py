import csv
f = open('populationbyage.csv')
data = csv.reader(f)
next(data); next(data); next(data)

a = 0; b=0; c=0;d=0;e=0;f=0;

for row in data:
    row[1:] = map(int, row[1:])
    a += row[3]
    b += row[8]
    c += row[13]
    d += row[23]
    e += row[28]
    f += row[33]
    
result = [a, b, c]
result2 = [e,d,f]
print(result, result2)

import matplotlib.pyplot as plt
plt.figure(dpi = 300)
plt.rc('font', family='Malgun Gothic')
plt.title('분기별 취업자 수 (천명)')
plt.plot(['1/4', '2/4', '3/4'], result, label = '2019년')
plt.plot(['1/4', '2/4', '3/4'], result2, label = '2020년')
plt.legend()
plt.show()


