'''

이번에는 append를 !!

'''

# 이미 있는 파일을 새로 쓰지 않고 거기다가 추가하고 싶을 때

file = open('hello.txt', 'at') # 이게 append의 의미 !!

file.write('Hello again.\n')
file.write('Nice to meet you again.\n')
print('hello.txt 파일에 새로운 내용이 추가되었습니다.')

file.close()
