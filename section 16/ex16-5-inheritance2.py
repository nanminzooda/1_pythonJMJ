class A:
    def greeting(self):
        print('안녕하세요. A입니다.')

class B(A):
    def greeting(self):
        print('안녕하세요. B입니다. ')


class C(A):
    def greeting(self):
        print('안녕하세요. C입니다. ')

class D(B, C):
    pass # 그냥 상속만 두 개 받은 클래스, 내부동작 필요없고 껍데기만 필요할 때 pass를 사용한다. 개념적으로 클래스를 제작한다.

x = D()

x.greeting()
# 실행을 시켜보면 B가 실행이 되네요 ?

print(D.mro())
# 이걸 찍어보면 확인할 수 있다. 순서를. 근데 이런식으로 애초에 코딩을 안하는게 나음. 지저분함.