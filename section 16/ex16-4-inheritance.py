'''

상속
    어떤 클래스가 가지고 있는 기능을 그대로 물려받아
    사용할 수 있는 클래스

사용방법 !!

class 슈퍼클래스 # 부모클래스 라고 부르기도 한다.
    본문

class 서브클래스 (슈퍼클래스)

'''

# 슈퍼클래스
class Coffee:
    def __init__(self, bean): # 생성자 만든거에요 알지?
        self.bean = bean
    def coffee_info(self):
        print('원두 : {}'.format(self.bean))

# 서브클래스
class Espresso(Coffee):
    def __init__(self, bean, water):
        super().__init__(bean) # 슈퍼를 썼다는 건 슈퍼클래스의 생성자를 사용하겠다는 의미 !
        self.water = water
    def espresso_info(self):
        super().coffee_info()
        print('물 : {}mL'.format(self.water))

coffee = Espresso('콜롬비아', 30)
coffee.espresso_info()

# 서브 클래스가 부모 클래스도 호출할 수 있다.
coffee.coffee_info()

# 원래 갖고있던 기능을 포함한다.