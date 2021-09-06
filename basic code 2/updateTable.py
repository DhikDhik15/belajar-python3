from database import *

sql = "UPDATE EMPLOYEE SET INCOME = INCOME + 10000 WHERE ID = 1"

try: 
    cursor.execute(sql)
    connection.commit()
except:
    connection.rollback()