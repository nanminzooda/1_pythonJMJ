file = open('hello.txt', 'rt')

while True:
    str = file.read(5)
    print(str)
    if not str:
        break # 비어있으면 트루가 된다 ? ... 읽을게 없으면 벗어나게 된다. 인덱스 값 가지는 튜플 등에서도 쓰인다.
    print(str, end='')

# 5글자씩 읽어주고 있다. (\n 때문에 약간 다르게 나올 수 있움) 의심되면 이렇게 찍어보기.

file.close()