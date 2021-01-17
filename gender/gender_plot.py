# 꺾은선 그래프 
import csv

f=open('gender.csv')
data=csv.reader(f)

m=[];f=[]

#name = input('찾고 싶은 지역의 이름을 알려주세요 : ')
name = '강남'
for row in data:
    if name in row[0]:
        print(name+'동 포함된 지역 :', row[0])
        for i in range(3,104):
            m.append(int(row[i]))
            f.append(int(row[i+103]))
        break;
            
import matplotlib.pyplot as plt
plt.plot(m, label='Male')
plt.plot(f, label='Female')
plt.legend()
plt.show()
