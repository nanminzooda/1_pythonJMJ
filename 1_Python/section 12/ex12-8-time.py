'''

time 모듈
    시간 처리에 관련된 모듈 time

'''

import time

# 1970년 1월 1일 0시 0분 0초부터 현재까지 경과 시간을 반환
# 마이크로초 까지!! 와우!!

print(time.time())

# ctime() 함수 - 인수로 전달된 time 시간 형식을 갖춰 반환
print(time.ctime(time.time())) # 외국 바이브로다가 반환해주신다.

# 인수로 전달된 날짜와 지시자를 이용하여 형식을 갖춘 날짜 데이터를 반환한다. !!
print(time.strftime('%Y-%m-%d %H:%M:%S')) # 여기서 %라고 한 것이 지시자.
print(time.strftime('%Y{} %m{} %d{} %H:%M:%S'.format('년', '월', '일'))) # 여기서 %라고 한 것이 지시자.

# 와 ! 유니코드 !!!
print(time.strftime('%Y년 %m월 %d일').encode('unicode-escape').decode())

# 인자 초 만큼 시스템을 일시정지 시킬 수 있습니다. 키키

time.sleep(1)

# 이것을 이용해서 시간 세는 것을 만들어보겠어용.

sec=1

while True:
    print(sec)
    if sec==10:
        break
    time.sleep(1)
    sec+=1

# 와 ! 이렇게 하면 카운트 세는 프로그램을 만들 수 있다 !
