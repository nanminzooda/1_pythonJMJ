class Calculator:

    def input_expr(self):
        expr = input('수식을 입력하세요 >>>')
        self.expr = expr

    def calculate(self):
        return eval(self.expr) # eval 은?
    # 수식이 따옴표로 인식되어서 인풋 함수로 들어가서 !! 이거 그래도 꽤 사용하긴 함 !! 프론트(사용자들이 움직이는 곳) !! 에서 ㅋㅋ.


# 일단 변수를 선언하기.
calc = Calculator() # 객체 선언 했음.

calc.input_expr()
print('수식 결과는 {}입니다.'.format(calc.calculate())) # 이렇게 꼭 !! calc.calculate로 객체를 타고 들어가야 한다.
# 컨트롤 누르고 클릭하면 그 레퍼런스로 간다 대박신기행

# format 도 하나으ㅣ 메소드.

# ㅎㅎ 오늘도 재밌었다.