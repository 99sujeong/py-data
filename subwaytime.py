import csv
f = open('subwaytime.csv')
data = csv.reader(f)
next(data); next(data)
'''
result = []

# 지하철 시간대별 이용현황
for row in data:
    row[4:] = map(int, row[4:])
    result.append(row[10])
print(len(result))
print(result)


# 아침 7~9시 승차 인원 더하기
for row in data:
    row[4:] = map(int, row[4:])
    result.append(sum(row[10:15:2]))
print(len(result))
print(result)


import matplotlib.pyplot as plt
result.sort()
plt.style.use('ggplot')
plt.bar(range(len(result)), result)
plt.show()

# 지하철 7~9시(출근시간) 승차 인원 최대 역 찾기
mx = 0
mx_station = ''
for row in data:
    row[4:] = map(int, row[4:])
    if sum(row[10:15:2]) > mx:
        mx = sum(row[10:15:2])
        mx_station = row[3] + '(' + row[1] + ')'
print(mx_station, mx)

# 지하철 6~8시(퇴근시간) 하차 인원 최대 역 찾기
max = 0
max_station = ''
for row in data:
    row[4:] = map(int, row[4:])
    if sum(row[33:36:2]) > max:
        max = sum(row[33:36:2])
        max_station = row[3] + '(' + row[1] + ')'
print(max_station, max)

# 시간대별 최대 승차 역 이름 및 승차 인원 출력
mx = [0] * 24
mx_station = [''] * 24
for row in data:
    row[4:] = map(int, row[4:])
    for i in range(24):
        a = row[i * 2 + 4]
        if a > mx[i]:
            mx[i] = a # 시간대별 최대승차인원
            mx_station[i] = row[3] # 시간대별 최대승차인원 역이름
print(mx_station)
print(mx)

import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
plt.bar(range(24), mx)
plt.xticks(range(24), mx_station, rotation=90)
plt.show()
'''
# 지하철 시간대별 승하차 인원 추이
s_in = [0] * 24; s_out = [0] * 24
for row in data:
    row[4:] = map(int, row[4:])
    for i in range(24):
        s_in[i] += row[4 + i * 2] # 시간대별 승차인원
        s_out[i] += row[5 + i * 2] # 시간대별 하차인원

import matplotlib.pyplot as plt
plt.figure(dpi = 300)
plt.rc('font', family='Malgun Gothic')
plt.title('지하철 시간대별 승하차 인원 추이')
plt.plot(s_in, label = '승차')
plt.plot(s_out, label = '하차')
plt.legend()
plt.xticks(range(24), range(4, 28))
plt.show()




