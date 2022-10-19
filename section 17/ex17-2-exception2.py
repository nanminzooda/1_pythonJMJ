'''

예외 !!
    프로그램에 존재하는 오류와 비슷하지만
    개발자가 직접 처리할 수 있는 간단한 문제를 예외라고 한다.

사용법 !!
try:
    코드 작성영역
except:
    예외 발생 시 처리 영역

'''

try:
    a=int(input('제수를 입력하세요>>>'))
    b=int(input('피제수를 입력하세요>>>'))
    print('{} / {} = {}'.format(a, b, a/b))

    print('예외가 발생해도 실행이 되나 !?') # 이 문장은 예외가 생기면 걍 출력이 안되요 코드 자체를 갖다버리는거임.
except:
    print('예외가 발생했습니다.')

# try 에서 에러가 나면 걍 exception이 실행된다 !