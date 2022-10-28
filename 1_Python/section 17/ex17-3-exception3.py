'''

에러를 구체화시킬 수 있다.

'''

try:
    a=int(input('제수를 입력하세요>>>'))
    b=int(input('피제수를 입력하세요>>>'))
    print('{} / {} = {}'.format(a, b, a/b))

    print('예외가 발생해도 실행이 되나 !?') # 이 문장은 예외가 생기면 걍 출력이 안되요 코드 자체를 갖다버리는거임.
except ZeroDivisionError:
    print('예외가 발생했습니다. 0으로는 나눌 수 없습니다.')
except ValueError:
    print('예외가 발생했습니다. 정수만 입력할 수 있습니다.')
except:
    print('에러가 발생했습니다. 모든 에러.')
