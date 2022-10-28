'''

입출력! 와웅!

I/O (파일 입출력)
(input / output)
    입력(Input) 기존파일 읽어들이는 것
    출력(output) 파일생성, 내용 추가를 말한다.

'''

file = open('myFile.txt', 'wt') # wt 나 wd 를 사용하기도 한다. 여러가지 방법이 있다.
print('myFile.txt 파일이 생성되었습니다.')

# 파일은 마지막에 꼭 닫아줘야 해요.
file.close() # 닫지 않으면 메모리 에러나 파이썬 충돌이 발생하 수도 있습니다.호호
# myFile 이라는 파일(텍스트) 생겼음을 확인할 수 있다.

# with 문 - 자동으로 close()를 해준다. 딱히 클로즈를 해주지 않아도 된다.!!
with open('myFile.txt', 'wt') as file:
    print('myFile.txt 파일이 생성되었습니다.')
    # 위의 코드와 완전히 동일한 내용을 수행함



