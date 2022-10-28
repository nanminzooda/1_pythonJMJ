'''

random - 난수 생성 모듈!!

'''

import random
# 두 인수 사이의 난수를 ㅎㅎ

print(random.randint(1,10)) # 1~10 사이 난수가 나옵니다. 호호 (10도 포함함!!)

# range 함수
print(random.randrange(10)) # 1~9 사이 난수가 나옵니다. 위랑 약간 다르네용 ~
print(random.randrange(1, 10)) # 1~9 사이 난수가 나옵니다. ~

print(random.randrange(1, 10, 2)) # 1~9 사이의 홀!!쑤!! 스텝이니까 !!!! 지금은 스텝이 2니까 13579

# 0이상 1미만
print(random.random()) # 소수점으로 나와요. 여기에 100을 곱하면 확률이 나오니깤ㅋㅋㅋ 가챠 같은거 만들 때 재밌음.

if random.random()<5:
    print('집행검을 획득하였습니다.')
else:
    print('다음기회를 사용하세요.')

# 이런식으로 획득할 수 있게 ㅋㅋ 만들 수 있다. 가챠. ㅋㅋ.

# choice 함수
seasons = ['spring', 'summer', 'fall', 'winter']
print(random.choice(seasons))
# 리스트 안의 값이 하나가 랜덤으로 나온다. !!

# shuffle() 함수 - 임의로 섞는 함수
my_list=[1,2,3,4,5]
random.shuffle(my_list)
print(my_list)
# 쉽게 이해할 수 있다. 리스트를 섞어버립니다 히히.

