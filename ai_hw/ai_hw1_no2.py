'''
문제2. 월과 일을 입력받아 1월 1일부터 그날까지의 날짜수를 계산하는 코드를 작성하시오.
'''

m=int(input('몇 월인지 숫자를 입력해주세요 :'))

if m not in range(1,12+1):
    while True:
        m=int(input('월(month)을 다시 입력해주세요. 1~12에 해당하는 숫자를 입력하셔야 합니다. :'))
        if m in range(1,12+1) :
            break

n=int(input('몇 일인지 숫자를 입력해주세요 :'))

if n not in range(1,28+1):
    while True:
        n=int(input('일(day)을 다시 입력해주세요. 1~28에 해당하는 숫자를 입력하셔야 합니다. :'))
        if n in range(1,28+1) :
            break

day=0

list_31=[1,3,5,7,8,10,12]
list_30=[4,6,9,11]

for i in range(1,m) :
    if i in list_31 :
        day+=31
    elif i in list_30 :
        day+=30
    else :
        day += 28

finalday=day+n

print('입력하신 날 까지의 날짜는 총 {}일 입니다.'.format(finalday))
