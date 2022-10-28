'''

List
    단일 변수에 여러 항목을 저장하는 데 사용된다.
    리스트 항목은 순서가 지정되고 변경 가능하며 중복 값을 허용한다.
    리스트에는 다양한 데이터 유형이 포함될 수 있다.

'''

thislist=['피카츛','라이츛', '꼬부기']
print(thislist)
print(thislist[0])

# 리스트 길이
print(len(thislist))

# list에는 데이터 유형을 맘대로 넣을 수 있지롱

list1=['피카츛','라이츛', '꼬부기']
list2=[1,2,3,4,5]
list3=[True, False]

# 다양한 유형 포함 가능

# 항목 접근

thislist=['피카츛','라이츛', '꼬부기']
print(thislist[1])

# 변경도 가능하지롱 아주쉽지롱

thislist[1]='잠만보'
print(thislist)

# 슬라이싱 인덱싱을 이용해서 통째로 대체할 수도 있다.

thislist=['피카츛','라이츛', '꼬부기']
thislist[1:3]=['울먹이','메타몽']
print(thislist)

# 두 번째 ; 두 개를 날려버리고 하나로 대체할 수도 있다.

thislist=['피카츛','라이츛', '꼬부기']
thislist[1:3]=['울먹이']
print(thislist)

# 항목 추가도 가능해용

thislist=['피카츛','라이츛', '꼬부기']
thislist.append('꼬부기')
print(thislist)

# 지정된걸 넣고싶으면 인서트를 이용하면 됩니다.

thislist=['피카츛','라이츛', '꼬부기']
thislist.insert(1,'잠만보')
print(thislist)

# 항목 제거도 당근 가능하죠 크크

thislist=['피카츛','라이츛', '꼬부기']
thislist.remove('꼬부기')
print(thislist)

# 위에서는 값 자체로 제거한 것입니다

# 항목에 지정된 인덱스로 제거하는 것도 가능 !

thislist=['피카츛','라이츛', '꼬부기']
thislist.pop(2)
print(thislist)

# 인덱스를 지정하지 않으면 제일 마지막에 있는 값이 제거된다.

thislist=['피카츛','라이츛', '꼬부기']
thislist.pop(2)
print(thislist)

# 문법상 에러가 나지는 않지만 실행하면 에러가 난다.

# del thislist
# print(thislist)

# 목록 삭제

thislist=['피카츛','라이츛', '꼬부기']
thislist.clear()
print(thislist)

# 호호 하나만 더 배워봅시다; 확장

thislist=['apple', 'banana']
thislist.extend(['cherry', 'mango'])
print(thislist) # 뒤에 붙인게 추가 되었어요 ㅎㅎ
