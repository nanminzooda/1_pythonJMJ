'''

내장함수를 배워볼거에요
    구글링을 해보시면 찾아볼 수 있습니다.

eval
    매개변수로 받은 expression (=식) 을 문자열로 받아서, 실행하는 함수

'''

expr=input('계산식을 입력하세요 :')
result=eval(expr)

print(expr + '=' + str(result))

# 문자열을 계산식으로 인식해서 계산해주는 함수이기 때문에 아무거나 입력하면 결과가 오류가 납니다 !