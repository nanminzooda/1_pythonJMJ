'''

새로 배운 내용으로 예제 풀기 !

'''

import random
import time

# 일단 두 개의 모듈을 불러온 것.

pot = [n for n in range(1,46)] # 리스트를 만들었다. 팟 !
jackpot = [] # 잭팟이라는 빈 리스트를 만들었다. 잭팟 !

for n in range(1, 7): # 1부터 6까지 돈다. !
    random.shuffle(pot) # 섞는다. !
    pick = pot.pop() # 메소드. 값을 돌려준다. pop()은 마지막거 하나를 돌려준다. 근데 순서를 모르니까 랜덤으로 뽑은거랑 똑같음.
    print('{}번째 당첨 번호는 {}입니다.'.format(n, pick))
    jackpot.append(pick) # 잭팟 리스트에 집어넣고.
    time.sleep(2) # 긴장감을 위해 2초간 쉬어가기 ㅎㅎ.

jackpot.sort()
print('이번 당첨 번호는 {}입니다.'.format(jackpot))

# ㅋㅋ 로또 번호 제공해줄 수 있다. // 예제 !! 해보자.