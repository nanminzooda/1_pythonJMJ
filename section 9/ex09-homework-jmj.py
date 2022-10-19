# 회원가입을 시작합니다.

id = str(input('ID를 입력 하세요. (3글자 이상) >>>'))
# id라는 문자열도 집합성이 있으므로 반복문을 돌리는 객체가 될 수 있다.

while True:
    if len(id) >=3:
        print('사용가능한 ID입니다.\n')
        break
        # 받을 때 까지 반복해야 하면 이렇게 while 문을 바깥에 쓰는게 효과적이구나.
    else:
        id = str(input('잘못된 입력입니다. 3글자 이상 입력 하세요. >>>'))



pw = str(input('PassWord를 입력 하세요. (영문 숫자 포함 8글자 이상) >>>'))
ch_count_pw = 0
num_count_pw = 0

while True:
    for ch in pw:
        if ch.isalpha():
            ch_count_pw += 1
            # 알파벳이 몇 개 있는지
        elif ch.isnumeric():
            num_count_pw += 1
            # 숫자가 몇 개 있는지

    if ch_count_pw > 0 and num_count_pw > 0 and len(pw)>=8 :
        print('사용가능한 PassWord 입니다.')
        pw_again = str(input('PassWord를 다시 한번 입력하세요. >>>'))
        if pw_again == pw:
            print('회원가입이 완료되었습니다.\n')
            break
        else:
            pw = str(input('일치하지 않습니다. PassWord를 처음부터 다시 입력하세요. >>>'))
            continue
    else:
        pw = str(input('잘못된 입력입니다. 영문 숫자 포함 8글자 이상 입력하세요. >>>'))

# if랑 while을 크게 그려서 큰그림을 보고 써야한다 while문 남발하면 코드에서 빠져나갈 수가 없음.

print('로그인을 시도합니다.')

inid=input('ID를 입력하세요>>>')

while True:
    if inid == id:
        break
    else:
        inid=input('ID가 일치하지 않습니다. 다시 입력하세요. >>>')

inpwd=input('PassWord를 입력하세요>>>')

while True:
    if inpwd == pw:
        print('로그인이 완료되었습니다. ')
        break
    else:
        inpwd=input('PassWord가 일치하지 않습니다. 다시 입력하세요. >>>')