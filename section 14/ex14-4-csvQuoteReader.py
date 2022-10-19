member_list=[]
with open('회원명단.csv', 'rt', encoding='UTF-8') as file : # 인코딩 문제 해결
    file.readline()
    while True:
        line = file.readline()
        if not line:
            break
        member = line.split(',')
        member[0] = member[0].strip('"') # strip; 공백을 제거 !
        member_list.append(member)

print(member_list)

# 다시 말하지만 csv는 콤마로 구분 !