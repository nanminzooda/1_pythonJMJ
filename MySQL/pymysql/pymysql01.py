# step 1 = pymysql 모듈 불러오기

import pymysql

# step 2 = Mysql Connection 연결
#(하이디sql 에서 연결 했듯이 여기서도 해 줘야 한다.)

con=pymysql.connect(
    host='127.0.0.1',
    user='scott',
    password='tiger',
    db='hr',
    charset='UTF8')

# step 3 = Connection 으로 부터 Cursor 생성 (명령어를 불러오고 실행해주는 애)

cur = con.cursor();

# step 4 = Sql문 실행

sql = 'SELECT empno, ename, job FROM emp'
cur.execute(sql)

# 데이터 Fetch
rows = cur.fetchall();
print(rows)

# step 5 = DB 연결 종료 ! 필수 !

con.close()

