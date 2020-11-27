# 내림차순

'''
ages=[17,14,18,13,19]

for x in range(0,len(ages)):
    max=ages[x]
    p=x
    for i in range(x, len(ages)):
        if ages[i] >= max:
            max=ages[i]; maxp=p
        p+=1
    
    temp=ages[x]; ages[x]=ages[maxp]; ages[maxp]=temp

print(ages)
'''
# 함수 연습 - 1~n까지 더하기
n=10
def tsum(n):
    mysum=0
    for i in range(1, n+1):
        mysum=mysum+i
    return (mysum)

t=tsum(10); print(t)
t=tsum(20); print(t)
t=tsum(30); print(t)

# 리스트원소 더하기
def tsum(mylist):
    mysum=0
    for i in mylist:
        mysum=mysum+i
    return (mysum)

mylist=[10,20,30,40,50]
t=tsum(mylist); print(t)

# 리스트원소 찾기
def tsearch(mylist, n):
    for i in mylist:
        if n == i:
            return ('yes')
            break;
    return ('no')

mylist=[10,20,30,40,50]
t=tsum(mylist,50); print(t)

# 리스트원소 가장 큰 값 찾기
def tsum(mylist):
    for i in mylist:
        if n == i:
            return ('yes')
            break;
    return ('no')

mylist=[10,20,30,40,50]
t=tsum(mylist); print(t)
