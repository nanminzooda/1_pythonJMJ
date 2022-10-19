def get_average(marks):
    total = 0
    for subject in marks:
        total += marks[subject]
        # 딕셔너리 객체임을 바로 알아야 한다.
        # 딕셔너리는 포 문에 키 값이 들어간다.

    average = total / len(marks)
    # 이때의 average는 지역변수
    return average


marks = {'국어': 90, '영어': 80, '수학': 84}
average=get_average(marks)
# 이때의 average는 전역변수
print('평균은 {}점 입니다.'.format(average))

# 딕셔너리를 넣으면 평균 점수를 반환한다.