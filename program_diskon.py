## Program untuk menghitung potongan harga

# tampilan awal
print ("================================")
print ("-KASIR TOKO RENTAL DVD PAK KADES")
print ("================================")

# daftar harga barang
dvd1 = int(50000)
dvd2 = int(30000)
dvd3 = int(80000)
dvd4 = float(50500)

print (f"1 ) AVENGER : LEGEND OF KORRA 6    = Rp{dvd1:,.2f}")
print (f"2 ) BATTLEFIELD XII                = Rp{dvd2:,.2f}")
print (f"3 ) GRANRED FANTASY : METAL RISING = Rp{dvd3:,.2f}")
print (f"4 ) IMMORTAL COMBAT x              = Rp{dvd4:,.2f}")
print ("================================")

# input jumlah barang
bar1 = int(input("BERAPA BANYAK UNTUK DVD 1? : "))
bar2 = int(input("BERAPA BANYAK UNTUK DVD 2? : "))
bar3 = int(input("BERAPA BANYAK UNTUK DVD 3? : "))
bar4 = int(input("BERAPA BANYAK UNTUK DVD 4? : "))

# proses total
total1 = bar1 * dvd1
total2 = bar2 * dvd2
total3 = bar3 * dvd3
total4 = bar4 * dvd4

total_all = total1 + total2 + total3 + total4

print ("================================")
print (f"TOTAL : Rp{total_all:,.2f}")

# pilihan diskon
disc1 = 0.1
disc2 = 0.2
disc3 = 0.5

print ("================================")
print ("DISKON YANG TERSEDIA : ")
print ("1 ) DISKON 10%")
print ("2 ) DISKON 20%")
print ("3 ) DISKON 50%")
print ("================================")

disc_sel = int(input("PILIH DISKON : "))

# proses diskon
disc_val = 0

if disc_sel == 1:
    disc_val = total_all * disc1
elif disc_sel == 2:
    disc_val = total_all * disc2
elif disc_sel == 3:
    disc_val = total_all * disc3
else:
    print ("DISKON TIDAK TERSEDIA")
    
totalhar = total_all - disc_val

print (f"TOTAL HARGA : Rp{totalhar:,.2f}")

# pembayaran
print ("================================")
bayar = float(input("MASUKKAN NOMINAL PEMBAYARAN : Rp"))

kmb = bayar - totalhar

# output
print ("================================")
print ("DETAIL TRANSAKSI : ")
print ("ITEM 1 : ", bar1)
print ("ITEM 2 : ", bar2)
print ("ITEM 3 : ", bar3)
print ("ITEM 4 : ", bar4)
print (" ")
print (f"TOTAL  : Rp{total_all:,.2f}")
print (f"DISKON : Rp{disc_val:,.2f}")
print (f"NOMINAL BAYAR : Rp{bayar:,.2f}")
print (" ")
print (f"TOTAL HARGA : Rp{totalhar:,.2f}")
print (f"TOTAL KEMBALIAN : Rp{kmb:,.2f}")
print ("================================\n")

## credit and disclaimer

print ("\nProgram ini dikembangkan oleh :")
print ("Rasya Pramudya Teja - 2025310027\n")
