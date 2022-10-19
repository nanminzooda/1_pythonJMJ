'''

for 문
    값의 범위나 횟수가 정해져있을 때 사용하면 편리한 반복문
    while 문보다 자주 사용한ㄷ.

for 변수 in 반복가능한 객체 :
    반복 실행문
'''

pwd = input('비밀번호를 입력하세용 ! :')

ch_count=0
num_count=0

# pwd 라는 문자열도 집합성이 있으므로 반복문을 돌리는 객체가 될 수 있다.
for ch in pwd:
    if ch.isalpha():
        ch_count += 1
        # 알파벳이 몇 개 있는지
    elif ch.isnumeric():
        num_count += 1
        # 숫자가 몇 개 있는지
if ch_count >0 and num_count >0:
    print('가능한 비밀번호 입니다.')
else:
    print('불가능한 비밀번호 입니다. ')

# 그러니까 내말은, 비밀번호에다가 알파벳 하나이상 쓰고 숫자도 하나 이상 사용하라는 거지.