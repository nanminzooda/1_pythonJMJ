'''

method 를 계속해서 배워보자구.

'''

# join() 메소드
s='-'.join('python')
print(s) # 문자열 사이사이에 조인 하겠다.

# 문자열 뿐만 아니라 리스트에도 사용 가능하다.
s='-'.join(['a', 'b', 'c', 'd', 'e'])
print(s) # 문자열처럼 묶어서 뱉어버린다.

s=''.join(['a', 'b', 'c', 'd', 'e'])
print(s) # 문자열처럼 묶어서 뱉어버린다.

s=''.join({'a':'apple', 'b':'banana'})
print(s)
# 키만 뱉어주는 ㅎㅎ.

# split() 메소드 (많이 사용한다.)
s='Life is too short'
result=s.split()
print(result) # 메소드가 귀찮아도 ... 다양한 기능을 알고 있어야 하니까.
# split 은 '문자열을 찢어서 리스트로 반환' 합니다.

s='010-5015-0973'
result=s.split('-')
print(result) # 주어진 것을 기준으로 잘라서 리스트를 반환한다. 정말 많이 사용합니다.

# replace()
s='Life is too short'
result=s.replace('short', 'long')
print(result)

# strip(), lstrip(), rstrip() 이것들은 공백제거 !!
s='          apple'
print(s)

result=s.lstrip()
print(result)

s='apple             '
print(s)

result=s.rstrip()
print(result)

s='        apple             '
print(s)

result=s.strip()
print(result) # 양 쪽의 모든 공백을 제거한다.

# 다른 방식으로 잔뜩 끼어있는 공백을 죽이고 싶다면 ?? 공백을 공백 아닌것으로 replace
s =' a p p l e j e o n g w o o'
print(s)
result=s.replace(' ', '')
print(result)
