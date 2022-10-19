'''
문제 3.

숫자를 (10부터 100) 입력받아 그 수에 해당하는 개수만큼의 1부터 10까지의 정수형 데이터(1차원)를 생성하고,

그 평균과 분산, 데이터분포를 출력하는 과정을 반복하는 코드를 작성하시오.

단 입력이 0이면 멈추고, 10~100과 0이 아닌 입력일 때는 범위가 맞을 때까지 다시 입력받는다.
'''

import numpy as np

n=int(input('10부터 100까지의 숫자를 입력해주세요 :'))
anslist=[]

if n==0:
    print('0을 입력하셨기 때문에 종료합니다.')
elif n not in range(10,100):
    while True :
        n=int(input('다시 입력하세요:'))
        if n in range(10,100):
            for i in range(1, n + 1):
                a = np.random.randint(1, 11)
                anslist.append(a)
            print(np.mean(anslist))
            print(np.var(anslist))
            print(anslist)
            break
        elif n==0:
            print('0을 입력하셨기 때문에 종료합니다.')
            break
else:
    for i in range(1,n+1):
        a=np.random.randint(1,11)
        anslist.append(a)
    print(np.mean(anslist))
    print(np.var(anslist))
    print(anslist)
