'''
• 문제4. 크기가 10x7이고 평균이 80, 표준편차가 15인 데이터를 생성하고,
각 열별로, 그리고 각 행별로 최대값과 그 최대값이 있는 위치를 출력하는 코드를 작성하시오.
'''

import numpy as np

array=np.random.normal(loc=80, scale=15, size=(10,7))
print(array) # 생성한 행렬 데이터

print(np.max(array, axis=0)) # 각 열별 최대값 리스트
print(np.argmax(array, axis=0)) # 각 열별 최대값의 위치 리스트

print(np.max(array, axis=1)) # 각 행별 최대값 리스트
print(np.argmax(array, axis=1)) # 각 행별 최대값의 위치 리스트