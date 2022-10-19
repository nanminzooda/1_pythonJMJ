# join() 메소드
s = '-'.join('python')
print(s)

s = '+'.join(['a', 'b', 'c', 'd', 'e'])
print(s)

s = ''.join(['a', 'b', 'c', 'd', 'e'])
print(s)

s = ''.join({'a': 'apple', 'b': 'banana'})
print(s)

# split() 메소드
s = 'Life is too short'
result = s.split()
print(result)

s = '010-1234-5678'
result = s.split('-')
print(result)

# replace()
s = 'Life is too short'
result = s.replace('short', 'long')
print(result)

# strip(), lstrip(), rstrip() 공백제거
s = '     apple'
print(s)
result = s.lstrip()
print(result)

s = 'apple     '
print(s)
result = s.rstrip()
print(result)

s = '     apple     '
print(s)
result = s.strip()
print(result)

# 전체 공백제거
s = ' a p p l e '
print(s)
result = s.replace(' ', '')
print(result)


