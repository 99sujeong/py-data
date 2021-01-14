# 항아리 모양 그래프
import csv

f=open('gender.csv')
data=csv.reader(f)

m = []
f = []

name = input('찾고 싶은 지역의 이름을 알려주세요 : ')
#dong = '신도림'
'''
for row in data:
    if dong in row[0]:
        for i in range(0, 101):
            m.append(int(row[i+3]))
            f.append(int(row[-(i+1)]))
f.reverse()
'''
for row in data:
    if name in row[0]:
        print(name+'동 포함된 지역 :', row[0])
        for i in row[3:104]:
            m.append(-int(i))
        for i in row[106:]:
            f.append(int(i))
            
import matplotlib.pyplot as plt
'''
plt.barh(range(101), m)
plt.barh(range(101), f)
'''
plt.style.use('ggplot')
plt.figure(figsize=(10,5), dpi=300)
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False
plt.title(name+' 지역의 남녀 성별 인구 분포')
plt.barh(range(101), m, label='남성')
plt.barh(range(101), f, label='여성')
plt.legend()
plt.show()
