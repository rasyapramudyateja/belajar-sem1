print ("=" *30)
print ("YAYASAN PEDULI DENGAN MANUSIA")
print ("=" *30)
print ("PROGRAM KONVERSI NILAI")

nama = input("MASUKKAN NAMA ANDA :")
nilai = int(input("MASUKKAN NILAI DENGAN FORMAT NUMERIK :"))    
status = 0
value = 0

if nilai >= 85:
    value = "A"
    value = "B"
elif nilai >= 55:
    value = "C"
elif nilai >= 40:
    value = "D"
else:
    value = "E"
    
if nilai >= 55:
    status = "SELAMAT ANDA LULUS"
else:
    status = "MAAF ANDA MASIH BELUM BERHASIL"

print ("=" *30)
print ("HASIL KONVERSI DAN STATUS ANDA SAAT INI")
print ("=" *30)

print ("NAMA : ", nama)
print ("STATUS NILAI ANDA : ", value)
print (status)
