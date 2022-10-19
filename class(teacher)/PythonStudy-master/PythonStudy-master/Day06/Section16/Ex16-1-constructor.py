'''
파일명 : Ex16-1-constructor.py

생성자
    인스턴스를 생성할 때 생성자가 자동으로 호출된다.
    객체 초기화 용으로 사용한다.
'''

class USB:

    # 생성자
    def __init__(self, capacity):
        self.capacity = capacity
        print('USB 생성자가 호출되었습니다.')

    def info(self):
        print('{}GB USB'.format(self.capacity))

usb = USB(64)
# usb.info()




