# 신도림 인구 구조 시각화
import csv

f=open('age.csv')
data=csv.reader(f)

result = []

# '신도림'
dong = input('동 이름 입력 =>')

for row in data:
    if dong in row[0]:
        for i in row[3:]:
            result.append(int(i))
    
print(result)

import matplotlib.pyplot as plt
plt.style.use('ggplot') # 격자 무늬 스타일
plt.plot(result)
plt.show()

