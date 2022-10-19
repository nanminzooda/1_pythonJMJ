import json

with open('dictList.json', 'r') as file:
    json_reader = file.read()
    dict_list = json.loads(json_reader)

for dic in dict_list:
    print('이름: {}'.format(dic['name']))
    print('나이: {}'.format(dic['age']))
    print('키: {}'.format(dic['spec'][0]))
    print('몸무게: {}'.format(dic['spec'][1]))
    print()

# 구글 검색은 필수 !! 원초적인 로우 레벨 언어가 바로 C!!
# C는 몰라도 되긴함. // 개발 한다고 해서 모든 언어를 다 필요하진 않다. ( ㅎㅎ근데 보안 쪽에서는 C가 필수 )
# 보안 어렵댈요 삶이 어려워질 수 있음ㅋㅋ. 적성에 잘 맞다면 그것을 해봐도 좋음 !! 킼킼 재밌겠다.
# C를 알아야 하는 이유 ; C가 기본이라서. 로우 언어. 제일 원초적임. 뭐가 나와도 대비할 수 있음.

# section 18 부터는 프로젝트임. 이게 벌써 끝나간다 이거에요.