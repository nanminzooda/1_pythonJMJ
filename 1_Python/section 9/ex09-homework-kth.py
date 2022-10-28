id = None
pwd = None

# 아이디 입력

while True:
    id = input('아이디를 입력하세요. (3글자 이상) >>>')
    if len(id) >= 3:
        break
    print('> 3글자 이상 입력해주세요.')

# 패쓰워드 입력

while True:
    pwd = input('패쓰워드를 입력하세요 (영문, 숫자 포함 8자 이상) >>>')
    isContainAlpha = False
    isContainNumeric = False

    for ch in pwd:
        if ch.isalpha():
            isContainAlpha=True
        elif ch.isnumeric():
            isContainNumeric=True
    if not isContainAlpha or not isContainNumeric or len(pwd)<8 :
        print('> 영문, 숫자 포함 8자 이상 입력해주세요!')
        continue
        # 이 밑이 실행되지 않는다는 것을 알 수 있다.

    pwdChk = input('패쓰워드를 한번 더 입력하세요. >>>')
    if pwd != pwdChk:
        print('일치하지 않습니다. 다시 입력해주세요.')
        continue
        # 이렇게 되면 그냥 반복문의 맨 처음으로 아예 돌아가게 됩니다. 이 밑을 건너뛰게 되므로 이 반복문을 탈출하지 못한다.
    break

print('회원가입 완료!')

# 로그인

while True:
    loginid=input('아이디를 입력하세요. >>>')
    if id==loginid:
        break
    print('> 아이디가 일치하지 않습니다. ')

# 로그인 패쓰워드

while True:
    loginPwd=input('패쓰워드를 입력하세요. >>>')
    if pwd==loginPwd:
        break
    print('패쓰워드가 일치하지 않습니다.')

print('로그인 완료 !')