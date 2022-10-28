from sqlalchemy import create_engine
import pandas as pd

db_connection_str='mysql+pymysql://scott:tiger@127.0.0.1/hr?charset=utf8mb4'
db_connection = create_engine(db_connection_str)
conn=db_connection.connect()

sql="select * from emp"

result = pd.read_sql_query(sql,conn)
print(pd.DataFrame(result))

conn.close()

# ID랑 PW는 왜 필요한걸까용 ?? 클라이언트 아닌가 그냥?

# 판다스 때문에 예쁘게 나와용