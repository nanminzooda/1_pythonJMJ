file = open('hello.txt', 'at')

file.write('Hello.\n')
file.write('Nice to meet you.\n')
print('hello.txt 파일에 새로운 내용이 추가 되었습니다.')
file.close()