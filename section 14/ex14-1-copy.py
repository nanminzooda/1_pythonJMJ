'''

파일 복사
    원본 -> 변수(메모리) -> 복사본

'''

buffer_size = 1024 # 1024Byte로 1kB를 의미합니다. # 컴퓨터는 16진수 !

with open('hello.txt', 'rb') as source: # with를 쓰면 닫을 필요 없다
    with open('hello2.txt', 'wb') as copy:
        while True:
            buffer = source.read(buffer_size) # 요사이즈 단위로 읽는다는 ! 너무 한꺼번에 읽으면 컴퓨터에 과부하가 걸릴 수도 있어서.
            # 네트워크 통신 시 버퍼 사이즈를 정해서 속도를 조절할 수 있다.
            if not buffer: # 즉 buffer == '' 일 때
                break
            copy.write(buffer)

print('hello2.txt 파일이 복사되었습니다. ')
