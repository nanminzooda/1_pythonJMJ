'''

datetime
    날짜와 시간 데이터를 처리할 때 사용한다.
'''

import datetime

# 현재 날짜와 시간 변환 마이크로초 단위 출력

print(datetime.datetime.now())
# 현재 시간에 관련한 출력을 무엇으로 할 것인지는 잘 생각해보고 !! 취향에 따라. !!

print(datetime.datetime.today())

# date() 함수 특정 날짜를 만들어 반환
print(datetime.date(2022,9,28))

# time() 함수 특정 시간을 만들어 반환
print(datetime.time(10,48,0))

# 날짜 필드값
print(datetime.datetime.now().year)
print(datetime.datetime.now().month)
print(datetime.datetime.now().day)
print(datetime.datetime.now().hour)
print(datetime.datetime.now().minute)
print(datetime.datetime.now().second)
# 이렇게 한 부분부분만 뽑아낼 수도 있다.


# timedelta 날짜/시간 데이터 연산

today=datetime.datetime.now()
yesterday=today-datetime.timedelta(days=1)
print(yesterday)
tomorrow = today + datetime.timedelta(days=1)
print(tomorrow)

date1 = datetime.date(2022, 8, 25)
date2 = datetime.date(2022, 9, 28)

print(date2 - date1) # 와 이렇게 하면 디데이를 !!
print((date2-date1).total_seconds()) # 이건 그 디데이를 초로 계산했을 때 !!