'''

method 와 string 을 배워보겠습니다.

메소드(method)란
    특정 객체가 가지고 있는 함수를 의미한다.
    객체명.메소드명() 이런식으로 사용한다. 내장함수랑 사용이 약간 다름. 객체에 종속되어 있다는 것이 특징.

'''

# String 객체 format 메소드
print("10자리 폭 왼쪽 정렬 '{:<10d}'".format(123))
print("10자리 폭 오른쪽 정렬 '{:>10d}'".format(123))
print("10자리 폭 가운데 정렬 '{:^10d}'".format(123))
print()
print("10자리 폭 왼쪽 정렬 채움 문자 '{:*<10d}'".format(123))
print("10자리 폭 오른쪽 정렬 채움 문자 '{:*>10d}'".format(123))
print("10자리 폭 가운데 정렬 채움 문자 '{:*^10d}'".format(123))

# 포맷 메소드 함수 앞에 달린 것 자체가 객체 (문자열 자체)

# count() 메소드 라는 게 있어요

s = '내가 그린 기린 그림은 목이 긴 기린 그림이고, 네가 그린 기린 그림은 목이 짧은 기린 그림이다.'
result=s.count('기린')
print(result)
# 메소드 함수 입니다! 기린이라는 단어가 몇 개가 들어가있는지 세 주는 함수!

s='best of best'
result=s.count('best', 5) # 이렇게 되면, 인덱스가 1인 위치부터 찾는다는 말이다.
print(result)

result='best of best'
result=s.count('best', -7) # 이렇게 되면, 인덱스가 1인 위치부터 찾는다는 말이다.
print(result)

# find() 메소드 -> 위치 반환 !

s='apple'
result=s.find('p')
print(result)

# 없는 값은 ??

s='apple'
result=s.find('z')
print(result)
# find 내장함수 에서는 없는 값을 찾으라고 하면 '-1'을 뱉습니다.

# index 라는 내장함수 !!

s='apple'
result=s.index('z')
print(result)
# index 내장함수 에서는 없는 값을 찾으라고 하면 오류를 만들어냅니다. !! 오류 원해요 ?! 원할 때 사용하면 좋다.
# index와 find는 비슷한 메소드지만 원하는 문자가 없을 때 드러나는 반응이 다르다 !! 에러가 필요한지 아닌지 ~~!!

