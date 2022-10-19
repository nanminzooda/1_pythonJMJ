file = open('hello.txt', 'rt')

line_list = file.readlines()
# 리스트로 받을 수 있다 ! 포문이랑 리스트는 항상 중뇨해요

for line in line_list:
    print(line, end='')

file.close()