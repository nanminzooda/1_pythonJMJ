'''
mutable - 메모리 값을 변경할 수 있다.
    리스트, 세트, 딕셔너리
'''

me=[1,2,3]
print(me) # 주소값에 접근해서 가져온다.
print(id(me))

me.append(4)
print(id(me))

# mutable 의 경우, 값을 추가해도 주소가 변하지 않는다는 것을 알 수 있다.

'''
immutable - 메모리 값을 변경할 수 없다. 
     튜플, 정수 int, 실수 float, 문자열 string
'''

me = 10
print(id(me))

me += 1
print(id(me))
# 새로운 공간을 할당해서 덧셈을 해소하는 방식. 그래서 주소가 변한다는 것을 알 수 있다.