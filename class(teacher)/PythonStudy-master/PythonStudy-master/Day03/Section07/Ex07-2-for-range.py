'''
파일명 : Ex07-2-for-range.py

for 문과 range 함수
'''
dan = int(input('출력할 구구단을 입력하세요 >>> '))
for n in range(1, 10):
    print('{} x {} = {}'.format(dan, n, dan * n))