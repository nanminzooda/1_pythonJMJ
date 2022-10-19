file = open('hello.txt', 'rt')

# 요것은 좀 많이 사용하는 편 !

while True:
    str = file.readline() # 이번엔 줄 단위로 읽어용
    print(str)
    if str == '':
        break
    print(str, end='')

file.close() # 안닫으면 안되는거에용 !