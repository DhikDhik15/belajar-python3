from database import *

cursor = connection.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
   LAST_NAME, AGE, SEX, INCOME)
   VALUES ('Red', 'Poco', 11, 'S', 50000)"""
try:
   # Execute the SQL command
   cursor.execute(sql)

   # Commit your changes in the database
   connection.commit()

except:
   # Rollback in case there is any error
   connection.rollback()

# disconnect from server
#connection.close()