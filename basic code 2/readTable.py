from database import *

# Prepare SQL query to INSERT a record into the database.
sql = "SELECT * FROM EMPLOYEE" 
try:
   cursor = connection.cursor()

   # Execute the SQL command
   cursor.execute(sql)
   
   # Fetch all the rows in a list of lists.
   # Fetchone () - Ini mengambil baris berikut dari kumpulan hasil query.
      # Set hasil adalah objek yang dikembalikan saat objek kursor digunakan untuk query tabel.
   # Rowcount - Ini adalah atribut read-only dan mengembalikan jumlah baris yang dipengaruhi oleh metode execute ().
   
   results = cursor.fetchall()
   for row in results:
      print("List Employee \n",row)
except :
   print ("Error: unable to fetch data")
