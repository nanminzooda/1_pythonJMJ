'''
datetime
    날짜와 시간 데이터를 처리할 때 사용한다.
'''

import datetime

# 현재 날짜와 시간 변환 마이크로초 단위 출력
print(datetime.datetime.now())
print(datetime.datetime.today())

# date() 함수 특정날짜를 만들어 반환
print(datetime.date(2022,9,28))

# time() 함수
print(datetime.time(10,48,0))

y = datetime.datetime.now().year
m = datetime.datetime.now().month
d = datetime.datetime.now().day
print('{}년 {}월 {}일'.format(y,m,d))

# 날짜 필드값
print(datetime.datetime.now().year)
print(datetime.datetime.now().month)
print(datetime.datetime.now().day)
print(datetime.datetime.now().hour)
print(datetime.datetime.now().minute)
print(datetime.datetime.now().second)

# timedelta 날짜/시간 데이터 연산
today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)
print(yesterday)
tomorrow = today + datetime.timedelta(days=1)
print(tomorrow)

date1 = datetime.date(2022, 8, 25)
date2 = datetime.date(2022, 9, 28)
print(date2 - date1)
print((date2 - date1).total_seconds())
