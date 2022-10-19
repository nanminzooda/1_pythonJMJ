import random
import time

pot = [n for n in range(1, 46)]
jackpot = []

for n in range(1, 7):
    random.shuffle(pot)
    pick = pot.pop()
    print('{}번째 당첨번호는 {}입니다.'.format(n, pick))
    jackpot.append(pick)
    time.sleep(2)

jackpot.sort()
print('이번 당첨번호는 {} 입니다'.format(jackpot))