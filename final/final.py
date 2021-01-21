import csv
f = open('onlineshopping.csv')
data = csv.reader(f)
next(data); 

total = []; internet = []; moblie = []

# 합계, 인터넷쇼핑, 모바일쇼핑 => 온라인 쇼핑 동향
for row in data:
    row[2:] = map(int, row[2:])
    if row[0] == '합계':
        if row[1] == '계':
            for i in row[2:]:
                total.append(i)
        elif row[1] == '인터넷쇼핑':
            for i in row[2:]:
                internet.append(i)
        else:
            for i in row[2:]:
                moblie.append(i)

# 그래프
import matplotlib.pyplot as plt
plt.figure(dpi = 300)
plt.rc('font', family='Malgun Gothic')
plt.title('분기별 온라인 쇼핑 동향')
plt.plot(['2019 1/4', '2019 2/4', '2019 3/4', '2020', '2020 1/4', '2020 2/4', '2020 3/4'], total, label = '계')
plt.plot(['2019 1/4', '2019 2/4', '2019 3/4', '2020', '2020 1/4', '2020 2/4', '2020 3/4'], internet, label = '인터넷쇼핑')
plt.plot(['2019 1/4', '2019 2/4', '2019 3/4', '2020', '2020 1/4', '2020 2/4', '2020 3/4'], moblie, label = '모바일쇼핑')
plt.legend()
plt.show()
