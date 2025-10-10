## Program untuk menghitung gaji karyawan
# Program ini dapat digunakan untuk menghitung gaji bersih karyawan

# tampilan awal menu
print ("==================================")
print ("-PROGRAM PENGHITUNG GAJI KARYAWAN-")
print ("==================================")

# input identitas karyawan
namkar = str(input("MASUKKAN NAMA KARYAWAN    : "))
pos    = str(input("MASUKKAN POSISI KARYAWAN  : "))
print ("----------------------------------")

# input gaji pokok, tunjangan, potongan
gp = float(input("MASUKKAN JUMLAH GAJI POKOK : Rp"))
tj = float(input("MASUKKAN JUMLAH TUNJANGAN  : Rp"))
pt = float(input("MASUKKAN JUMLAH POTONGAN   : Rp"))
print ("----------------------------------")

# proses kalkulasi gaji bersih
gb = gp + tj - pt

# Output
print ("BERIKUT ADALAH PERHITUNGAN GAJI DARI KARYAWAN ANDA : ")
print ("----------------------------------")
print ("NAMA KARYAWAN   : ", namkar)
print ("POSISI KARYAWAN : ", pos)
print (" ")
print (f"GAJI POKOK : Rp{gp:,.2f}")
print (f"TUNJANGAN  : Rp{tj:,.2f}")
print (f"POTONGAN   : Rp{pt:,.2f}")
print ("----------------------------------")
print (f"TOTAL GAJI BERSIH : Rp{gb:,.2f}")

## credit and disclaimer

print ("\nProgram ini dikembangkan oleh :")
print ("Rasya Pramudya Teja - 2025310027\n")
