'''

객체(object)란
    현실 세계에 존재하는 물리적, 추상적 모든 것들을
    프로그램으로 표현한 것
    예) 학생, 자동차, 컴퓨터, (물리적) // 주문, 배송, (추상적)(개념상 존재하는 것)
    어떻게보면 최소의 프로그램 단위. 느낌. !? (자바에서)

객체 구성
    속성 값 - 변수
    기능 - 메소드(함수) // 객체에 종속되어 있으면 메소드, 아니면 함수 // 둘은 크게 다르지 않음

'''

# Computer Class 정의 ! 킼킼 약간 붕어빵 틀.

class Computer :
    # 클래스는 첫 글자를 대문자로 적어주는 것이 좋다.
    # 첫 번째 매개변수가 self 이므로 인스턴스 메소드이다.
    # self를 제외한 나머지 매개변수에 실제로 사용될 데이터가 전달된다.
    def set_spec(self, cpu, ram, vga, ssd): # 여기서 self는 자기자신 클래스를 의미한다.
        self.cpu = cpu
        self.ram = ram
        self.vga = vga
        self.ssd = ssd

    def hardware_info(self):
        print('CPU={}'.format(self.cpu))
        print('RAM={}'.format(self.ram))
        print('VGA={}'.format(self.vga))
        print('SSD={}'.format(self.ssd))

desktop = Computer()

# self 는 인스턴스 메소드 임을 나타낼 뿐이라서 굳이 안적어도 된다.
desktop.set_spec('i7', '16GB', 'GTX3060', '512GB')
print(desktop.cpu)

desktop.hardware_info()
# 이렇게 하면 그냥 컴퓨터 사양이 나옵니다.

macbook = Computer()
macbook.set_spec('M2', '16GB', 'intel', '512GB')

# desktop 이랑 macbook 는 형태만 유사하지 완전히 다른 데이터. 변수랑 메소드를 모아놓은 덩어리로 생각하면 된다. 계속 사용할 수 있다.
# 원하는 것을 만들어낼 수 있다. 코드 재사용이 유리하다. 

'''
# 함수로 하는거 보여줄까 ? 함수로 하면 컴퓨터 라는 어떠한 구심점으로 묶는 게 불가능해진다.

cpu=''
ram=''
vga=''
ssd=''

def set_spec1(cpu, ram, vga, ssd):  # 내가 함수를 보여줄게
    cpu = cpu
    ram = ram
    vga = vga
    ssd = ssd

set_spec1('i7', '16GB', 'GTX3060', '512GB')
print(cpu)
'''
