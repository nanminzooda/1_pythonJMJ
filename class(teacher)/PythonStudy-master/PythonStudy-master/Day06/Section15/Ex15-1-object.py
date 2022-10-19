'''
객체(Object)란
    현실 세계 존재하는 물리적, 추상적 모든것들을 
    프로그램으로 표현한 것.
    예) 학생, 자동차, 컴퓨터, 주문, 배송

객체 구성
    속성 값 - 변수
    기능 - 메소드(함수)
'''


# Computer 클래스 정의
class Computer:

    # 첫번째 매개변수가 self 이므로 인스턴스 메소드 이다.
    # self를 제외한 나머지 매개변수에 실제로 사용될 데이터가 전달된다.
    def set_spec(self, cpu, ram, vga, ssd):
        self.cpu = cpu
        self.ram = ram
        self.vga = vga
        self.ssd = ssd

    def hardware_info(self):
        print('CPU = {}'.format(self.cpu))
        print('RAM = {}'.format(self.ram))
        print('VGA = {}'.format(self.vga))
        print('SSD = {}'.format(self.ssd))


desktop = Computer()
desktop.set_spec('i7', '16GB', 'GTX3060', '512GB')
desktop.hardware_info()

macbook = Computer()
macbook.set_spec('M2', '16GB', 'intel', '512GB')
macbook.hardware_info()