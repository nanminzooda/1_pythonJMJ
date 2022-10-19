'''

에러가 난다고 해도 꼭꼭 실행하고싶은 코드가 있으면 어떻게 해요 !!??

try:
    코드 작성영역
except:
    예외 발생시 처리영역
else:
    예외가 발생하지 않으면 처리되는 영역
finally:
    언제나 실행되는 영역

'''

try:
    a=int(input('제수를 입력하세요>>>'))
    b=int(input('피제수를 입력하세요>>>'))

    result = a/b
    print('예외가 발생해도 실행이 되나 !?') # 이 문장은 예외가 생기면 걍 출력이 안되요 코드 자체를 갖다버리는거임.
except ZeroDivisionError:
    print('예외가 발생했습니다. 0으로는 나눌 수 없습니다.')
except ValueError:
    print('예외가 발생했습니다. 정수만 입력할 수 있습니다.')
except:
    print('에러가 발생했습니다. 모든 에러.')
else:
    print('{} / {} = {}'.format(a, b, result))
    # 이렇게 result를 따로 확인하기루 했거든
    # 에러가 안나면 실행이 되는거지. 어떤 에러도 실행되지 않은 경우에만.
finally:
    print('프로그램을 종료합니다.') # 에러가 난다고 해도 꼭 결국에는 실행해버리고싶은 구문이 있어요