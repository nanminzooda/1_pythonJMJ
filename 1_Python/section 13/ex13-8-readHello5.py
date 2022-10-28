file = open('hello.txt', 'rt')

line_list = file.readlines()
# 리스트로 받을 수 있다 ! 포문이랑 리스트는 항상 중뇨해요

for no, line in enumerate(line_list):
    print('{} {}'.format(no+1, line), end='')

file.close()

# enumerate 배웠음 복습하기
