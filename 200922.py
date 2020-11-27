"""
a=4
b=3
c=a+b
print(c)
print('hello')

# if문
if a > b: # 4 > 3 => True
    print("a가 크다")
else:
    print("b가 크다")


# while문
i = 1
while i <= 5:
    print(i)
    i += 1 

a = 1
b = 0
while a <= 5:
    b += a
    print(b)
    a += 1

# for문
b= 0
for c in [5,7,9]:
    b += c # b는 c를 합산
    print(c)
print(b) # 21


# input
print('start')
a = input('your name?') # 사용자 입력 받는 함수 
print('my name is ', a)


# 자료형
i = 10  # 정수형 / int
x = 10.5 # 실수형 / float

print(type(i))
print(type(x))

# 문자형
a = 'Hello World!'
b = 'Hello \n World!'
c = 'he said, "that\'s mine"'
print(a, b, c)

# 문자열 연산
a = 'abc'
b= 'def'
print(a+b)
print(a*2)
print(len(a))
"""

# 인덱싱
a = 'abcdef'
print(a[2])
print(a[-2])

# 슬라이싱
print(a[3:5])


# 문자열 포메팅
age = 5
print("I'm %d years old" % age)
