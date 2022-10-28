'''

지역변수랑 전역변수를 배울거에용
(local)  (global)

지역변수 local
    함수 내부 선언
    함수 내부에서만 사용 가능

전역변수 global
    함수 외부 선언
    함수 외부와 내부 모두에서 사용 가능

'''

gVar='전역'

def globalAndlocal():
    lVar='지역'
    gVar = '변경된 전역이 아닌 새로운 지역'
    print(gVar, '변수입니다.')
    # 전역 변수는 어디서나 사용
    # 현재는 참조만 하다가 값을 넣어버렸어.
    print(lVar, '변수입니다.')

globalAndlocal()

# print(lVar) # 이거 하면 오류나요. 저 안에만 들어있는 변수라성.

# 전역 변수를 함수 안에서 새롭게 옮겨버리면 바뀐다. 지역으로.
print(gVar)
# 보이지 ? 전역이라는 글자 그대로 나오는거 ??

# 그러면 함수 안에서 전역변수를 아예 뒤집어버리려면 ??

print()

# 전역 변수 선언
total = 0
wedding = {}

def gift(dic, who, money):
    global total
    # global 예약어를 사용해서 전역변수를 사용하겠다고 선언할 수 있다. 수정하고 싶으면 무조건 이렇게 해야함.
    total += money
    dic[who] = money # 딕셔너리에 키 값과 함께 값을 업데이트할 수 있다.

# wedding이라는 것 또한 전역변수로 생각하면 편하다.

gift(wedding, '정우', 100) # {'정우':100}
gift(wedding, '영희', 5) # {'정우':100, '영희':5}
gift(wedding, '철수', 5) # {'정우':100, '영희':5, '철수':5}
gift(wedding, '민지', 5)
print('축의금 명단:{}'.format(wedding))
print('전체 축의금:{}'.format(total))
# 전역 변수를 호출한 덕분에 total을 수정할 수 있었다. 아예. 함수 안에서도.

