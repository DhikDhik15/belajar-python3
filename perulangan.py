#while loop
count = 0
while(count < 4):
    print("count: ",count)
    count = count + 1
print("selesai")

#for loop
angka = [10,20,30,40,50]
for a in angka:
    print(a)

hobi = ['makan','tidur','jalan'] #akan diulang sebanyak data array yang didefinisikan
for m in hobi:
    print('hobi saya',hobi)

#Contoh penggunaan Nested Loop
#Catatan: Penggunaan modulo pada kondisional mengasumsikan nilai selain nol sebagai True(benar) dan nol sebagai False(salah)

i = 2
while(i < 100):
    j = 2
    while(j <= (i/j)):
        if not(i%j): break
        j = j + 1
    if (j > i/j) : print(i, " bilangan prima")
    i = i + 1

print("Selesai!")
