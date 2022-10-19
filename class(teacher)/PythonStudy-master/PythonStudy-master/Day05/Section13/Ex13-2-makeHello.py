'''
파일명 : Ex13-2-makeHello.py
'''
file = open('hello.txt', 'wt')
file.write('안녕하세요.')
file.write('\n')
file.write('반갑습니다.')
file.write('\n')
print('hello.txt 파일이 생성되었습니다.')
file.close()