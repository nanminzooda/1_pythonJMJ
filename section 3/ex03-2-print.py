'''

print() 함수 사용법 ㅎㅎ
    sep : 출력할 value의 구분 문자
    end : value 출력 후 출력할 문자 (기본값 '\n')
    file : 출력 방향 지정
    flush : flush 출력 유무 지정

'''

print('재미있는', '파이썬')
print('재미있는', '파이썬', sep=',')

print('안녕용', end='')
print('하셍용') # 기본값인 줄바꿈을 없애버렸지

fos=open('sample.py', mode='wt')
print('print("hello World")', file=fos)
# 파일에다가 저것을 적어버렸어용
fos.close()


