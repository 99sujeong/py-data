# 막대그래프
'''
import matplotlib.pyplot as plt
plt.bar([0, 1, 2, 4, 6, 10], [1, 2, 3, 5, 6, 7])
plt.show()

import matplotlib.pyplot as plt
plt.bar(range(6), [1, 2, 3, 5, 6, 7])
plt.show()
'''

# 인구 구조 시각화 - 막대그래프
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
plt.bar(range(101), result) # 수직 막대 그래프
plt.show()

plt.barh(range(101), result) # 수평 막대 그래프
plt.show()
