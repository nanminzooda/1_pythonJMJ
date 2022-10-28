'''

Tuple 튜플 !!
단일 변수에 여러 항목을 저장하는 데 사용된다 !
순서가 있고 변경할 수 없는 리스트 !
둥근 괄호로 작성된다 !

'''

thistuple=('피카츄', '라이츄', '파이리')
print(thistuple)

# 튜플의 길이도 당연히 알 수 있죵

thistuple=('피카츄', '라이츄', '파이리')
print(len(thistuple))

# 항목 가져오기 인덱싱으로 !!!

thistuple=('피카츄', '라이츄', '파이리')
print((thistuple[1]))
print((thistuple[1:3]))

# 변환이 안되는게 원칙이긴 한데, 바꾸고 싶다면 ?

thistuple=('피카츄', '라이츄', '파이리', '꼬부기')
thiscast=list(thistuple)
thiscast[1]='잠만보'
thistuple=tuple(thiscast)
print(thistuple)

# 아시겠죠? 튜플 타입은 원래 변경이 안되는 게 원칙입니다. 그래서 리스트를 거쳐서 가야 합니다.

# 이번에는 튜플 압축 풀기

thistuple=('피카츄', '라이츄', '파이리', '꼬부기')
(p1, p2, p3, p4)=thistuple

print(p1)
print(p2)
print(p3)
print(p4)

print(type(p1)) # 문자열로 나온다.

# 두 개의 튜플을 엮어보겠어용

thistuple1=('피카츄', '라이츄', '파이리', '꼬부기')
thistuple2=('버터풀', '야도란', '피존투', '또가스')
print(thistuple1+thistuple2)





