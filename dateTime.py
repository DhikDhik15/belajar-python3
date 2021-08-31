import time;  # Digunakan untuk meng-import modul time
import calendar; #import modul kalender

ticks = time.time()
print ("Berjalan sejak 12:00am, January 1, 1970:", ticks)

localtime = time.localtime(time.time())
print ("Waktu lokal saat ini :", localtime)

localtime = time.asctime( time.localtime(time.time()) )
print ("Waktu lokal saat ini :", localtime)

cal = calendar.month(2021, 9)
print ("Dibawah ini adalah kalender:")
print (cal)
