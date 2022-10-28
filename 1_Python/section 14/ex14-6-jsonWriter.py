'''

Jason 모듈을 사용할거에요

'''

# 첫 번째 실행

import json

dict_list=[
    {
        'name':'james',
        'age':20,
        'spec':[
            175.5,
            70.5
        ]

    },
    {
        'name':'Alice',
        'age':21,
        'spec':[
            168.5,
            60.5
        ]
    }
]

json_string = json.dumps(dict_list) # 문자열로 바꿔준 것
print(json_string)

# 요즘은 파이썬에서 이런 리스트로 정보를 주고받는다

with open('dictList.json', 'w') as file:
    file.write(json_string)

print('jason 파일이 생성되었씁니다. 하핫')