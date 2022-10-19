'''
 또 다른 예제를 풀어보자는겁니다 저는
'''

dan=2

while dan <=9:
    n=1
    while n<=9:
        print('{}X{}={}'.format(dan, n, dan*n), end='/')
        n+=1
    dan +=1
    print()

# 빈 공간을 넣어주면 좀 더 보기 편안해집니다. 데이터 베이스를 배울 때 반복문 없이도 할 수 있다. 