'''

continue
    while문이나 for문과 같은 반복문을 강제로 건너뛰기(아래의 코드를 실행하지 않는다. )
'''

total=0

for a in range (1,101):
    if a % 3 ==0:
        continue
    print('a:{}, total:{}'.format(a, total))
    # 이렇게 사이에 끼워넣어 주면 진짜 3의 배수만 빼고 더했다는 것을 확인할 수 있다.
    # 컨티뉴 때문에 'for문' 에서 빠진거임.
    total +=a

print(total)

# 3의 배수들은 더하기에 포함시켜 주지 않는다는 뜻 ~!

