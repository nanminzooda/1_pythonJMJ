file = open('hello.txt', 'wt')

file.write('hello this is JangMinju')
file.write('\n')
file.write('Python cant read Korean. so do not use Korean.')
file.write('\n')
file.close()

# 인코딩이라는 것 때문에 에러나는 경우가 가끔 있다. 사용자에게 보여질 때. 인코딩 문제.
# 개발자가 여러명이다보니 개발자들끼리의 인코딩이 다를 수 있고, 서버와의 인코딩 설정이 달라서 그럴수도 있다. 