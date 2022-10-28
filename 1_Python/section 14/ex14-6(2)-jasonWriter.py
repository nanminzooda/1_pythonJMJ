# 두 번째 실행

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

# 그니까 제이슨은 모듈이라 이거지 ??

# 제이슨 파일은 언제 사용해요 ? -> csv 파일이랑 유사해용.
# 키와 밸류 값으로 데이터를 저장할 때 가독성이 좋고 csv 보다 좋다. 데이터가 많아지면 편하게 데이터 확인 가능. <name>'jason'<\name>
# 어떤 어플에서는 제이슨파일로 데이터를 저장하고 백업하기도 한다.

json_string = json.dumps(dict_list, indent=4, ensure_ascii=False)
print(json_string)

with open('dictList.json', 'w') as file:
    file.write(json_string)

print('dictList.json 이라는 파일이 생성되었습니다.')