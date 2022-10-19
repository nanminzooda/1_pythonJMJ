file = open('hello.txt', 'rt')

while True:
    str = file.read(5)
    if not str:
        break
    print(str, end='')

file.close()