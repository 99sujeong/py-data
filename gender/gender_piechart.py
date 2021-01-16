# pie chart
'''
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
label=['A형', 'B', 'AB', 'O']
plt.axis('equal')
plt.pie([10, 30, 20, 50], labels=label, autopct='%.1f%%')
plt.show()
'''
import csv

f=open('gender.csv')
data=csv.reader(f)

size=[]

#name = input('찾고 싶은 지역의 이름을 알려주세요 : ')
name = '강남'
for row in data:
    if name in row[0]:
        m=0;f=0
        print(name+'동 포함된 지역 :', row[0])
        for i in range(101):
            m+=int(row[i+3])
            f+=int(row[i+106])
        break;
size.append(m); size.append(f)
print(size)
            
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
label=['남','여']
plt.title(name+' 지역의 남녀 성별 인구 분포')
plt.axis('equal')
plt.pie(size, labels=label, autopct='%.1f%%')
plt.show()
