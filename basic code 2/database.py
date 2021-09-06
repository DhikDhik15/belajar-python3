import pymysql.cursors

# Open database connection
connection = pymysql.connect(host='localhost',
                            user='dhika',
                            password='cliquers150193',
                            database='python3',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)


cursor = connection.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print ("Database version : %s " % data)
print ("Connected to",connection.host)