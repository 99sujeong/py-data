# 2019년 1월 지하철 유/무임 승하자
import csv
f = open('subwayfee.csv')
data = csv.reader(f)
next(data)
"""
mx = 0; rate = 0
for row in data:
    for i in range(4, 8):
        row[i] = int(row[i])
    if row[6] != 0:
        rate = row[4] / row[6]
    if rate > mx:
        mx = rate; name = row[3]
        #print(name, mx)

# 무임승차 비율이 가장 높은 곳
# row[6] / row[4] + row[6]
max = 0; r= 0;
for row in data:
    for i in range(4, 8):
        row[i] = int(row[i])
    if row[6] != 0:
        r = row[6] / (row[4] + row[6])
    if r > max:
        max = r; name = row[3]
print(name, max)

# 유임승차 비율이 가장 높은 곳
max = 0; r= 0;
for row in data:
    for i in range(4, 8):
        row[i] = int(row[i])
    if row[6] != 0 and (row[4] + row[6]) > 100000:
        r = row[4] / (row[4] + row[6])
    if r > max:
        max = r; mx_station = row[3] + ' ' + row[1]
print(mx_station, max)
"""
label = ['유임승차', '유임하차', '무임승차', '무임하차']
max = [0]*4; mx_station = ['']*4;
for row in data:
    for i in range(4, 8):
        row[i] = int(row[i])
        if row[i] > max[i-4]:
            max[i-4] = row[i]
            mx_station[i-4] = row[3] + ' ' + row[1]
for i in range(4):
    print(label[i]+':'+mx_station[i], max[i])
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
plt.pie(max, labels =label)
plt.show()
