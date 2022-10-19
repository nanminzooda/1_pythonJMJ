'''

enumerate
    List, Tuple, String 등 여러가지 자료형을 입력받으면
    인덱스 값을 포함하는 enumerate 객체를 돌려줍니다.
'''

months=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for month, day in enumerate(months):
    print('{}월={}일'.format(month +1, day))

# enumerate 가 인덱스랑 그 값을 같이 뽑아내줘서 위와 같이 출력할 수 있었어요.