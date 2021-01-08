#알고리즘
'''
n=int(input())
if (n%3==1):
    print(n, "3의 배수가 아니다.")
else:
    print(n, "3의 배수이다.")

m=352 # 거스름돈

#100원
m100=0
while m>=100:
    m100 += 1
    m-=100
print("100원 동전 =>", m100)

# 10원
m10 = 0
while m>=10:
    m10 += 1
    m-=10
print("10원 동전 =>", m10)

# 1원
m1 = 0
while m>0:
    m1 += 1
    m-=1
print("1원 동전 =>", m1)

# 80, 8, 1
m=352 # 거스름돈

# 80원
m80=0
while m>=80:
    m80 += 1
    m-=80
print("80원 동전 =>", m80)

# 8원
m8 = 0
while m>=8:
    m8 += 1
    m-=8
print("8원 동전 =>", m8)

# 1원
m1 = 0
while m>0:
    m1 += 1
    m-=1
print("1원 동전 =>", m1)
'''
# 검색, 정렬
ages = [17, 14, 18, 13, 19]

# 13?
key=13

found = False ##
position = 0 
for i in range(len(ages)):
    position+=1
    if ages[i] == key:
        found = True
        print("Y", position,"번째")
        break

if(not found):
    print('N')

# 가장 나이가 많은 값
max= 0
for age in ages:
    if age > max:
        max = age
print(max)

# 정렬
ages.sort()
print(ages)



