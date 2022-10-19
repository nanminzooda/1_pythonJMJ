'''
클래스변수
    클래스를 기반으로 만든 모든 인스턴스가 공유할 수 있는 변수


클래스메소드
    인스턴스가 없어도 클래스를 이용해 호출 할 수 있으며
    cls 이용해 클래스 변수를 사용할 수 있다.
'''

class Bag:
    count = 0

    def __init__(self):
        Bag.count += 1

    @classmethod
    def sell(cls):
        cls.count -= 1

    @classmethod
    def remain_bag(cls):
        return cls.count
    
    @staticmethod
    def slogan():
        print('명품 주인을 찾습니다.')


print('현재 가방: {}개'.format(Bag.remain_bag()))
bag1 = Bag()
bag2 = Bag()
bag3 = Bag()
print('현재 가방: {}개'.format(Bag.remain_bag()))
bag1.sell()
bag2.sell()
print('현재 가방: {}개'.format(Bag.remain_bag()))

Bag.slogan()






