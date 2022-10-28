'''

패키지
    모듈 상위 개념
    모듈의 집합을 의미한다

패키지 설치
console> pip install package명

패키지 삭제
console> pip uninstall package명

'''

import numpy as np
# 행렬 계산할 때 많이 쓰인다.

# 패키지를 설치하지 않으면 오류가 난다.
# 현재, venv 라는 폴더에서 별도로 파이썬을 실행하고 있는 중이다. 거기에다가 넘파이를 깔아야한다. pip를 통해서.
# 패키지끼리의 충돌을 방지하기 위해서 따로 공간을 설정한 것.

print(np.sum([1,2,3,4,5]))

# 넘파이는 패키지임
