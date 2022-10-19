'''
Set

순서가 없다
변경할 수 없다
인덱싱되지 않는 컬렉션. 왜냐 ? 순서가 없으니까

응용분야 : 로또 . ㅋㅋ. 번호 넣어놓고 인덱싱 해놓고 랜덤으로 숫자 얻기.


'''

thisset={'피카츄', '라이츄', ' 파이리'}
# 실행할 때 마다 순서가 변한다. 그래서 중복도 안된다.

print(thisset)

# 항목 가져오기

thisset={'피카츄', '라이츄', '파이리'}

# for 반복문 안에서도 순서는 없다.

for i in thisset:
    print(i)

# 값이 있는지 확인 ~!
thisset={'피카츄', '라이츄', '파이리'}
print('피카츄' in thisset)

# 항목 추가하기 !! 여기서는 add 함수를 사용해야하고, 여전히 순서가 없다.

thisset={'피카츄', '라이츄', '파이리'}
thisset.add('꼬부기')
print(thisset)

# 다른 Set의 항목 추가

thisset1={'피카츄', '라이츄', '파이리', '꼬부기'}
thisset2={'버터풀', '야도란', '피존투', '꼬부기'}

# 이렇게 두 셋트에서 중복이 있다면 걍 없애버린다. 따라서 set을 그냥 중복제거용으로 할 수도 있다.

thisset1.update(thisset2)
print(thisset1)

# 항목 제거 remove 쓰기 ~!

thisset={'피카츄', '라이츄', '파이리'}
thisset.remove('피카츄')
print(thisset)

# 근데 만약에 없는걸 지우라고 하면 리무브 함수는 오류가 나거든 ?? 그래서 디스카드를 쓰자.

thisset={'피카츄', '라이츄', '파이리'}
thisset.discard('피카츄')
print(thisset)
thisset.discard('피카츄')
print(thisset) # 에러가 나지 않습니다 ~! 없으면 없는대로 출력하는 편.

# 항목제거
# 근데 셋 에는 순서가 없는 만큼, 여기서는 랜덤 제거를 하게 된다.

thisset.pop()
print(thisset)

# 비우기 ~! 클리어

thisset.clear()
print(thisset)



