import sys

# sys module 을 가져올거고 이것은 운영체제랑 관련된 모듈

file = open('hello.txt', 'rt')

line_list = file.readlines()
sys.stdout.writelines(line_list)

# 운영체제 모듈

file.close()