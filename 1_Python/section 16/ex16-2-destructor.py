'''

생성자랑 다소 반대되는 개념 !! 소멸자 !!

소멸자
    인스턴스가 소멸될 때 자동으로 호출된다.
'''

class Service:
    def __init__(self, service):
        self.service = service
        print('{} Service가 시작되었습니다.'.format(self.service))

    def __del__(self):
        print('{] Service가 종료되었습니다.'.format(self.service))

s=Service('길 안내')
# 파이썬이 끝날때 쯤 종료된다.