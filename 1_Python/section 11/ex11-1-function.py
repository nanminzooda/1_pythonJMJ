'''

사용자 함수에 대해서 배워보겠어요
    사용자가 직접 만든 함수 !

def 함수이름(매개변수):
    본문
    return 반환값
    (return 이랑 매개변수는 없을수도 있다!)

'''

# welcome() 함수를 정의해봐요

def welcome():
    num1=10
    print(num1)
    # 프린트를 이렇게 중간중간 찍어줘야 어떤 값이 들어가있는지를 확인할 수 있습니다.
    num2=20
    print(num2)
    num3=num1+num2
    print(num3)
    print('hello python')
    print('nice to meet you')

welcome() # 함수를 불러요 !
# 리턴 값이 없기 때문에 그냥 프린트 하자는 것만 뱉고 끝납니다.

def introduce(name, age):
    print('내 이름은 {}이고 나이는 {}살입니다.'.format(name, age))

introduce('민주', 23)

# 대부분의 프로그래밍 언어는 변수와 함수로만 거의 이루어져있다.

# 매개변수가 정해져있지 않은 경우 ! 가변 매개변수를 사용합니다.

def show(*args):
    for item in args:
        print(item)

show('python', '아직은 재밌어', '그리고 정우는', '귀여워')

def address():
    str = '우편번호 12345\n'
    str += '서울시 동대문구 휘경동'
    return str

result=address()
print(result)

# 더하기 함수
def plus(num1, num2):
    return num1 + num2

print(plus(1, 2))

# 옆으로 한칸 이동 ! 내가 게임 캐릭터를 만들었지롱 히히
area=0
def move():
    return area+1

result=move()
print('유닛이 오른쪽으로 {}칸 이동했습니다.'.format(move()))