'''
파일명 : Ex12-2-module2.py
모듈 사용법 2
from 모듈명 import 함수
from 모듈명 import 함수1 , 함수2
from 모듈명 import *
'''
from converter import kilometer_to_miles

miles = kilometer_to_miles(150)
print('150km={}miles'.format(miles))