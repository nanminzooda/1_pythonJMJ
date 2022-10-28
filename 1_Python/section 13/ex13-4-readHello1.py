file = open('hello.txt', 'rt')

str = file.read()

print(str, end='')

file.close() # 꼭 !! 파일을 닫아쥬셔야 합니당.
# 파일에 들어가있는 것들이 모두 나왔어요 후후후
