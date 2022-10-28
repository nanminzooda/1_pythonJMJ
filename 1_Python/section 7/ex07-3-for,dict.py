'''

for이랑 딕셔너리를 사용해 볼 건데용 ㅎㅎ

'''

eng_dict={
    'sun':'태양',
    'moon':'달',
    'space':'우주',
}

# 딕셔너리는 리스트와 달리, 인덱스가 아니라 키 값 자체가 들어갑니다. !!

for word in eng_dict:
    print('{}의 뜻 : {}'.format(word, eng_dict.get(word)))

# 교재에서 다른 연습문제들 풀어보기 !