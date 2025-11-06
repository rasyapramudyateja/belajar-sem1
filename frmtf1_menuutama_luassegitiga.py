print ("=====MENU UTAMA=====")
print ("1. Konversi Nilai Numerik ke Alphabet")
print ("2. Cek Ganjil/Genap")
print ("3. Hitung Luas Segitiga")
print ("4. Keluar")

pilih = int(input("Pilih Menu (1/4) : "))

if pilih == 1:
    print ("PROGRAM TIDAK TERSEDIA")
elif pilih == 2:
    print ("PROGRAM TIDAK TERSEDIA")
elif pilih == 3:
    print ("PROGRAM KALKULASI LUAS SEGITIGA")
    print ("=" *30)
    alas = int(input("MASUKKAN ALAS :"))
    tinggi = int(input("MASUKKAN TINGGI :"))
    luas = 1 * alas * tinggi / 2
    print ("LUAS SEGITIGA ADALAH : ", luas, "cm2")
elif pilih == 4:
    print ("SAMPAI JUMPA")
