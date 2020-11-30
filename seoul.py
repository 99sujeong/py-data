# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 10:58:49 2020

@author: ansdb
"""

# 최고 기온 값 찾기
import csv
max_temp =-999   # 최고 기온 값을 저장할 변수
max_date =''       # 최고 기온이 가장 높았던 날짜를 저장할 변수
f =open('seoul.csv')
data = csv.reader(f)
header =next(data)
for row in data :
    if row[-1] =='' :
        row[-1] =-999   # -999를 넣어 빈 문자열이 있던 자리라고 표시
    row[-1] = float(row[-1])
    if max_temp < row[-1] :
        max_date = row[0]
        max_temp = row[-1]
f.close()
print('기상 관측 이래 서울의 최고 기온은',max_date+'로, ', max_temp, '도 였습니다.')

# 최저 기온 값 찾기
import csv
min_temp = 999   # 최저 기온 값을 저장할 변수
min_date =''       # 최저 기온이 가장 높았던 날짜를 저장할 변수
f =open('seoul.csv')
data = csv.reader(f)
header =next(data)
for row in data :
    if row[-2] =='' :
        row[-2] = 999   # 999를 넣어 빈 문자열이 있던 자리라고 표시
    row[-2] = float(row[-2])
    if min_temp > row[-2] :
        min_date = row[0]
        min_temp = row[-2]
f.close()
print('기상 관측 이래 서울의 최저 기온은',min_date+'로, ', min_temp, '도 였습니다.')
'''
# 8월의 온도값 조사
import csv
f = open('seoul.csv')
data = csv.reader(f)
next(data)
result = [ ]
for row in data :
    if row[-1] != '' :
        if row[0].split('-')[1] == '08' :
            result.append(float(row[-1]))
print(len(result)) # 전체 데이터 개수
import matplotlib.pyplot as plt
#plt.figure(dpi = 300)
plt.plot(result, 'hotpink')
plt.title('August max temperature')
plt.show()

# 1983년 이후 2월 14일 최고기온/최저기온 데이터로 그려보기
import csv

f = open('seoul.csv')
data = csv.reader(f)
next(data)
high = []
low = []

for row in data :
    if row[-1] != '' and row[-2] != '' :
        if 1983 <= int(row[0].split('-')[0]) :
            if row[0].split('-')[1] == '02' and row[0].split('-')[2] == '14' :
                high.append(float(row[-1]))
                low.append(float(row[-2]))

import matplotlib.pyplot as plt
#plt.figure(dpi = 300)
plt.plot(high, 'hotpink')
plt.plot(low, 'skyblue')
plt.show()

import csv
f = open('seoul.csv')
data = csv.reader(f)
next(data)
aug = []

for row in data :
    month = row[0].split('-')[1]
    if row[-1] != '' :
        if month == '08':
            aug.append(float(row[-1]))
print(len(aug)) # 8월 전체 최고기온
import matplotlib.pyplot as plt
#plt.figure(dpi = 300)
plt.hist(aug, bins = 100, color = 'r')
plt.show()
'''
# 8월 최고기온 boxplot - 그래프 크기 변경
import matplotlib.pyplot as plt
import csv
f = open('seoul.csv')
data = csv.reader(f)
next(data)

day = [[] for i in range(31)]

for row in data :
    if row[-1] != '' :
        if row[0].split('-')[1] == '08':
            day[int(row[0].split('-')[2])-1].append(float(row[-1]))
        
plt.style.use('ggplot')
plt.figure(figsize=(10,5), dpi=300)
plt.boxplot(day, showfliers=False)
plt.show()

# 1월 최고기온 boxplot - 그래프 크기 변경
import matplotlib.pyplot as plt
import csv
f = open('seoul.csv')
data = csv.reader(f)
next(data)

day = [[] for i in range(31)]

for row in data :
    if row[-1] != '' :
        if row[0].split('-')[1] == '01':
            day[int(row[0].split('-')[2])-1].append(float(row[-1]))
        
plt.style.use('ggplot')
plt.figure(figsize=(10,5), dpi=300)
plt.boxplot(day, showfliers=False)
plt.show()
