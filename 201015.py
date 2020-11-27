# 리스트원소 가장 큰 값 찾기
def tbig(mylist):
    mybig = mylist[0]
    for i in mylist:
        if i >= mybig:
            mybig = i
    return (mybig)

mylist=[40,30, 60, 70, 50]
t=tbig(mylist); print(t)

# 자판기 프로그램
print("〰"*8+"프친 푸드 가게"+"〰"*8)
print('1. 토스트(🍞) 1500원 2. 햄버거세트(🍔🍟🥤) 5300원 3. 피자(🍕) 9900원')

money = int(input("금액>>"))
menu = int(input("메뉴선택>>"))

if menu==1:
    money -= 1500
elif menu==2:
    money -= 5300
elif menu==3:
    money -= 9900
    
if money < 0:
    print("금액이 부족합니다")
else:
    won1000 = money//1000
    won500 = money%1000//500
    won100 = money%1000%500//100
    print("거스름돈: 1000원 {}개, 500원 {}개, 100원 {}개".format(won1000, won500, won100))
