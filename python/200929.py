# 반복문
"""
x = 0

x += 100
x += 100
x += 100
x += 100
x += 100 

print(x)

x = 0
for i in range(0, 5):
    x += 100
print(x)

y = 0
for i in range(1, 5):
    y += i
print(y)

score = [82, 73, 60, 12, 95]
sum = 0
for i in score:
    sum += i
    print(i)
print('sum=',sum)

n = 0
for i in score:
    if i >= 50:
        print(i, '50점 이상')
        n += 1
        if n >= 2:  break

for i in range(1, 10):
    print(2, '*', i, '=', 2*i)

dan = 3
for i in range(1, 10):
    print(dan, '*', i, '=', dan*i)

for dan in range(2, 10):
    for i in range(1, 10):
        print(dan, '*', i, '=', dan*i)


speed = 85
limit = 80

while speed > limit:
    print(speed, "...감속 필요...")
    speed -= 1
print(speed)


while True:
    print(speed, "...감속 필요...")
    speed -= 1
    if speed <= limit: break
print(speed)
"""

# 알고리즘
print("안녕")

sum = 20 + 30
avg = sum / 2
print('sum =',sum, ', avg =', avg)

input = int(input("숫자를 입력하세요 : "))
if input % 2 == 1:
    print("홀수이다")
else:
    print("짝수이다")
