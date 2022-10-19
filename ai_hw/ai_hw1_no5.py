'''
문제5.

크기가 (12,5)이고 값이 1~9 사이인 데이터를 생성하고,
값의 종류와 개수를 구하고,
각 열별로 최소값을 갖는 위치를 출력하는 코드를 작성하시오.
'''

import numpy as np

array=np.random.randint(1, 9+1, size=(12,5))
print(array)

n1=0
n2=0
n3=0
n4=0
n5=0
n6=0
n7=0
n8=0
n9=0

for n in range(0,12):
    for i in array[n]:
        if i == 1:
            n1 += 1
        elif i == 2:
            n2 += 1
        elif i == 3:
            n3 += 1
        elif i == 4:
            n4 += 1
        elif i == 5:
            n5 += 1
        elif i == 6:
            n6 += 1
        elif i == 7:
            n7 += 1
        elif i == 8:
            n8 += 1
        else:
            n9 += 1

print('해당 행렬에는 1이 {}개, 2가 {}개, 3이 {}개, 4가 {}개, 5가 {}개, 6이 {}개, 7이 {}개, 8이 {}개, 9가 {}개 있습니다.'.format(n1, n2, n3, n4, n5, n6, n7, n8, n9))

print(np.min(array, axis=0)) # 각 열별 최대값 리스트
print(np.argmin(array, axis=0)) # 각 열별 최대값의 위치 리스트
