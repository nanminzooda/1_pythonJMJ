'''

그 외의 내장함수 ㅎㅎ

'''

# format() !! 문자열로 !!

result = format(10000) # str(10000)과 같다
# 포맷 함수는 문자열로 바꾸는 기능이다.

result = format(10000, ',') # 천 단위 쉼표 ! 걍 끼워넣어주더라구용
print(result)

# abs() !! 절댓값 !!

result = abs(10)
print(result)
result = abs(-10)
print(result)

# max !! 최댓값 반환
# min !! 최솟값 반환

result = max(1,10)
print(result)

li=[5,7,8,6,4,2,7]

result=max(li)
print(result)

result=min(li)
print(result)

# pow !! 거듭제곱 함수 !!

result = pow(10, 2)
print(result)

# sorted !! 순서대로 정리해주세요 !!

my_li=[5,6,2,4,1,9,8]
result=sorted(my_li)
print(result)

# 거꾸로 정리하고 싶으면요 ?

result=sorted(my_li, reverse=True)
print(result)

names=['정우', '민주', '하늘', '귀여미']
scores=[60, 70, 80, 90]

for student in zip(names, scores):
    print(student)
    # 두 개의 리스트를 묶어서 튜플로 반환한다.

names=['정우', '민주', '하늘', '귀여미']
scores=[60, 70, 80, 90]

for name, score in zip(names, scores):
    print('{}의 점수는 {}점 입니다.'.format(name, score))

