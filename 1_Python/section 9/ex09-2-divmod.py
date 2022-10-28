'''

divmod
    두 숫자를 인자로 전달 받아 첫 번째 인자를 두 번째 인자로 나눈 몫과 나머지를
    tuple 형식으로 반환한다.

'''

money=10000
price=3000
result=divmod(money, price)

print('빵을 {}개 사고 {}원이 남았씁니다 ㅎㅎ'.format(result[0], result[1]))

# 그래서 현재 result 라는 건 튜플로 되어있답니다.