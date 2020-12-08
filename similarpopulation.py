import numpy as np
import csv
# 1. 데이터를 읽어온다.

f = open('age.csv')
data = csv.reader(f)
next(data)
data = list(data)

# 2. 궁금한 지역의 이름을 입력받는다.
name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요: ')
mn = 1 # 최솟값을 지정할 변수 생성 및 초기화
result_name = '' # 최솟값을 갖는 지역의 이름을 저장할 변수 생성 및 초기화
result = 0 # 최솟값을 갖는 지역의 연령대별 인구 비율을 저장할 배열 생성 및 초기화
home = [] # 입력 받은 지역의 데이터를 저장할 리스트 생성

# 3. 궁금한 지역의 인구 구조를 저장한다.
for row in data:
    if name in row[0]: # 입력 받은 지역의 이름이 포함된 행 찾기
        areaname = row[0]
        for i in row[3:]: # 3번 인덱스 값부터 슬라이싱 (0세~)
            home.append(int(i)) # 입력 받은 지역의 데이터를 home에 저장
        hometotal = int(row[2])
for k in range(len(home)):
    home[k] = (home[k]/hometotal)

# 4. 궁금한 지역의 인구 구조와 가장 비슷한 인구 구조를 가진 지역을 찾는다.
for row in data:
    away = []
    for i in row[3:]: # 3번 인덱스 값부터 슬라이싱 (0세~)
        away.append(int(i)) # 입력받은 지역의 데이터를 away에 저장
    awaytotal = int(row[2])
    for k in range(len(away)):
        away[k] = (away[k]/awaytotal)
    #print(row[0], away)
    sum = 0
    for i in range(len(away)):
        sum = sum + (home[i]-away[i])**2 # s = np.sum((homw - away)**2)
    #print(row[0], sum)
    if sum < mn and name not in row[0]:
        mn = sum
        result_name = row[0]
        result = away

# 5. 궁금한 지역의 인구 구조와 가장 비슷한 곳의 인구 구조를 시각화한다.
import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.figure(figsize = (10, 5), dpi = 300)
plt.rc('font', family='Malgun Gothic')
plt.title(name + '지역과 가장 비슷한 인구 구조를 가진 지역')
plt.plot(home, label = name)
plt.plot(result, label = result_name)
plt.legend()
plt.show()