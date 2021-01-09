ages = [17,14,18,13,19]
'''
#
small=ages[0]
p=0
for i in ages:
    if i <= small:
        small=i; smallp=p
    p+=1
print('small=', smallp, small)

##
ages[smallp]=99
small=ages[0]
p=0
for i in ages:
    if i <= small:
        small=i; smallp=p
    p+=1
print('small=', smallp, small)
print(ages)

###
ages[smallp]=99
small=ages[0]
p=0
for i in ages:
    if i <= small:
        small=i; smallp=p
    p+=1
print('small=', smallp, small)
print(ages)

####
ages[smallp]=99
small=ages[0]
p=0
for i in ages:
    if i <= small:
        small=i; smallp=p
    p+=1
print('small=', smallp, small)
print(ages)

#####
ages[smallp]=99
small=ages[0]
p=0
for i in ages:
    if i <= small:
        small=i; smallp=p
    p+=1
print('small=', smallp, small)
print(ages)
'''
## ages 리스트 파괴된다는 문제점 발생
oldages=ages
for x in range(0,len(ages)):
    small=ages[x]
    p=x
    for i in range(x, len(ages)):
        if ages[i] <= small:
            small=ages[i]; smallp=p
        p+=1
    
    temp=ages[x]; ages[x]=ages[smallp]; ages[smallp]=temp

print(ages)
    #print(small, end=' ')
    

