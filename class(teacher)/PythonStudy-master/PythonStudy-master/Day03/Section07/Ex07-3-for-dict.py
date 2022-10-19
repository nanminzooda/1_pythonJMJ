'''
파일명: Ex07-3-for-dict.py
for문 과 dict
'''
eng_dict = {
    'sun':'태양',
    'moon':'달',
    'star':'별',
    'space':'우주'
}
for word in eng_dict:
    print('{}의 뜻: {}'.format(word, eng_dict.get(word)))
