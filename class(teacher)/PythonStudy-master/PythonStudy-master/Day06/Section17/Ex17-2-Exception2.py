'''
파일명 Ex17-2-Exception2.py

예외
    프로그램 존재하는 오류 비슷하지만
    개발자가 직접처리 할 수 있는 간단한 문제를 예외라 한다.

try:
    코드 작성영역
except:
    예외 발생시 처리영역

'''

try:
    a = int(input('제수를 입력하세요 >>> '))
    b = int(input('피제수를 입력하세요 >>> '))
    print('{} / {} = {}'.format(a, b, a / b))

    print('예외 발생해도 실행됩니까?')
except:
    print('예외가 발생했습니다.')



















