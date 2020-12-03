import csv
f = open('populationbyage.csv')
data = csv.reader(f)
next(data); next(data)

a = 0; b=0; c=0;d=0;e=0;f=0;
a2 = 0; b2=0; c2=0;d2=0;e2=0;f2=0;
s_in = [0] * 6; s_out = [0] * 6
            
for row in data:
    row[1:] = map(int, row[1:])
    if '15 - 19세' in row[0]:
        for i in range(3):
            a += row[i * 5 + 3]
        s_in[0] = a
        for i in range(4,7):
            a2 += row[i * 5 + 3]
        s_out[0] = a2
    elif '20 - 29세' in row[0]:
        for i in range(3):
            b += row[i * 5 + 3]
        s_in[1] = b
        for i in range(4,7):
            b2 += row[i * 5 + 3]
        s_out[1] = b2
    elif '30 - 39세' in row[0]:
        for i in range(3):
            c += row[i * 5 + 3]
        s_in[2] = c
        for i in range(4,7):
            c2 += row[i * 5 + 3]
        s_out[2] = c2
    elif '40 - 49세' in row[0]:
        for i in range(3):
            d += row[i * 5 + 3]
        s_in[3] = d
        for i in range(4,7):
            d2 += row[i * 5 + 3]
        s_out[3] = d2
    elif '50 - 59세' in row[0]:
        for i in range(3):
            e += row[i * 5 + 3]
        s_in[4] = e
        for i in range(4,7):
            e2 += row[i * 5 + 3]
        s_out[4] = e2
    elif '60세이상' in row[0]:
        for i in range(3):
            f += row[i * 5 + 3]
        s_in[5] = f
        for i in range(4,7):
            f2 += row[i * 5 + 3]
        s_out[5] = f2
        
import matplotlib.pyplot as plt
plt.figure(dpi = 300)
plt.rc('font', family='Malgun Gothic')
plt.title('연령별 취업자 수')
plt.plot(['15-19세', '20-29세', '30-39세', '40-49세', '50-59세', '60세이상'], s_in, label = '2019년')
plt.plot(['15-19세', '20-29세', '30-39세', '40-49세', '50-59세', '60세이상'], s_out, label = '2020년')
plt.legend()
plt.show()