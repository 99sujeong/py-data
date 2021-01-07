# 리스트
rainbow = ['빨강', '주황', '노랑', '초록', '파랑', '남색', '보라']
print(rainbow)
print(type(rainbow))

a=['kim', 20]

# indexing
print(rainbow[0])
print(rainbow[-1])

# slicing
print(rainbow[2:5])
print(rainbow[2:])
print(rainbow[:2])

# index()
print(rainbow.index('노랑'))

# append()
c = []
c.append('park')
print(c)
c.append('kim')
print(c)
c.append('lee')
print(c)

# insert()
c.insert(1, 'gildong')
print(c)

# remove()
c.remove('park')
print(c)

# del
del c[1]
print(c)

# sort()
rainbow.sort()

# reverse()
rainbow.reverse()

# 리스트의 연산
b = ['park', 20]
print(a+b)
print(a*3)

# tuple
a = ('lee', 40, 20, 40)
print(a)

#dictionary
a= {1:'red'}
print(a)
a[2] = 'blue'
print(a)

mydict={'apple':'사과', 'banana':'바나나', 'orange':'오렌지'}
print(mydict['apple']) # key값으로 검색
mydict['pear'] = '배' # 값을 추가
print(mydict)

# 논리연산-비교연산자
print(1 < 2)
a =5; b = 6
print(a < b)
print(a <= b)
print(a == b)
print(a != b)

a = 'k'
b = 'x'
print(a > b)
print(a < b)
print(ord('x'))
print(chr(112))
       
a = 5
b = 6
print(a == b)
# a = b <- a에 b를 대입해라

# in 연산자
print(1 in [1, 2, 3])
print(5 in [1, 2, 3])

# and 연산
a = [1, 2, 3, 4, 5]
print((1 in a) and (6 in a))

# 아스키코드
mylist = ['apple', 'banana', 'Apple', 'APPLE']
print(sorted(mylist))

# not 연산
print(not True)
print(not False)

# if 조건문
a = True
if a:
    print('a is true')
else:
    print('a is False')

score = 71
if score >= 90:
    print("grade 1")
else:
    if score >= 80:
        print("grade 2")
    else:
        print("Fail")

if score >= 90:
    print("grade 1")
elif score >= 80:
    print("grade 2")
elif score >= 70:
    print("grade 3")
else:
    print("Fail")

score = 60
print("pass") if score >= 70 else print("fail")
    
