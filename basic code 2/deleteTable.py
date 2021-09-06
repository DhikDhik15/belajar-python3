from database import *

sql = "DELETE FROM EMPLOYEE WHERE ID = 1"

try:
    cursor.execute(sql)
    connection.commit()
except:
    connection.rollback()