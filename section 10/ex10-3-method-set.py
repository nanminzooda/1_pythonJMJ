'''

집합과 관련한 내용 !!

'''

# 교집합

s1={'apple', 'banana', 'cherry'}
s2={'apple', 'banana', 'orange'}
print(s1 & s2) # and 연산자로 교집합을 구해주었습니다.

result=s1.intersection(s2)
print(result)
# 결과는 동일합니다. 교집합을 구하는 일입니다.

# 합집합

s1={'apple', 'banana', 'cherry'}
s2={'apple', 'banana', 'orange'}
print(s1 | s2)

result=s1.union(s2)
print(result)
# 여기서도 결과는 동일합니다. 합집합을 구하는 일입니다!

# 차집합

s1={'apple', 'banana', 'cherry'}
s2={'apple', 'banana', 'orange'}
print(s1 - s2) # 빼기 연산자를 통해서 연산한다.

result=s1.difference(s2)
print(result)