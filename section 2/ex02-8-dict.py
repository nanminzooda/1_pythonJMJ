'''
Dictionary ~!
    key:value 형태로 이루어져있다. 쌍으로 데이터 ! 를 저장한다 !
    키값 중복 불가 !

'''

thisdict={
    "brand":"gucci",
    "model":"kai",
    "year":2022
}

print(thisdict)

'''
키 이름을 사용하여 참조할 수 있다는 점이 킬포 !
'''

# 값 가져오기
thisdict={
    "brand":"gucci",
    "model":"kai",
    "year":2022
}

print(thisdict['brand'])
print(thisdict.get('brand'))

# 키 목록 가져오기 !

print(thisdict.keys()) # 키 값을 리스트로 받아먹을 수 있다.

# 추가하기 !!!!

thisdict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}

thisdict['color']='red'
print(thisdict)

# 업데이트 라는 함수를 써도 된다 !

thisdict.update({'bgcolor':'black'})
print(thisdict)

# 변경하기 !~!~ 사실 업데이트는 만능! 있으면 변경이고 없으면 추가고 ~~

thisdict['color']='yellow'
thisdict.update({'bgcolor':'blue'})
print(thisdict)

# 제거하기 !!

thisdict.pop('model')
print(thisdict)





