'''

9월 28일 오늘은 모듈부터 !

모듈 (module)
    한 마디로 파이썬 파일(.py) 이다.
    모든 파일이 다 모듈이다.
    다른 파이썬 환경이나 콘솔에서 사용할 수 있음

    언제든지 변수나 함수 또는 클래스를 모아 놓은 파일을 모듈이라고 한다.
    한 마디로 파이썬 파일(.py) 이다.

모듈 사용법
import 모듈명

'''

import converter

miles = converter.kilometer_to_miles(150)
print('150km = {}miles'.format(miles))

pounds = converter.gram_to_pound(1000)
print('1000gram = {}pounds'.format(pounds))

# 파이썬은 모듈때문에 유명해졌다고 봐도 과언이 아님.

# 메소드는 객체에 종속되어있고 함수는 독립적으로 사용할 수 있다. 그 차이 뿐.