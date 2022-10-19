'''

모듈 사용법 2 !!

from 모듈명 import 함수

from 모듈명 import 함수1, 함수2

from 모듈명 import *

'''

from converter import kilometer_to_miles

miles = kilometer_to_miles(150)
print('150km={}miles'.format(miles))

# 아까랑 다른게 뭐냐고 ? 이번엔 모듈을 끼워서 가져온게 아니라 함수 자체를 불러온 것.
# 모듈명을 사용하지 않고도 함수만 부를 수 있다는 거지.