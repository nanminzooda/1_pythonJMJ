'''

확장자가 csv인 파일을 보신 적 있나요 ? 엑셀 같은거에서 보이기도 하거든요.

cvs; comma seperated values
    몇 가지 필드를 쉼표(,)로 구분한
    텍스트 데이터 및 텍스트 파일이다.

'''

student_list = []
with open('학생명단.csv', 'rt', encoding="UTF-8") as file: # 인코딩 매개변수를 찾아서 넣으니까 되네요. ...
    file.readline()
    while True:
        line = file.readline()
        if not line:
            break
        student = line.split(',')
        student_list.append(student)

print(student_list)

# 아무튼 안에 들어있는 데이터를 콤마로 잘라서 ! 엑셀 표 늒낌 ?