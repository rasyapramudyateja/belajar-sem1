## Program konversi mata uang Indonesia Rupiah (IDR) ke United States Dollar (USD)
# Program ini digunakan untuk mencari dan/atau mengubah 
# Nilai mata uang Indonesia (IDR) ke dalam nilai mata uang Amerika (USD) dan sebaliknya

## Menu tampilan dan input awal

print ("----------------------------------------")
print ("===IDR-USD CURRENCY CONVERTER PROGRAM===")
print ("----------------------------------------")
print ("PILIHAN KONVERSI : ")
print ("1 ) Indonesia Rupiah (IDR) - United States Dollar (USD)")
print ("2 ) United States Dollar (USD) - Indonesia Rupiah (IDR)")
pilih = int(input("PILIH : ")) # input pilihan menu program konversi
print ("----------------------------------------")

## Proses konversi dan output

kurs = int(16602) # nilai kurs IDR dalam USD saat ini

if pilih == 1: # jika memilih 1, maka akan masuk ke menu konversi IDR-USD
    pilih = int(input("MASUKKAN JUMLAH UANG DALAM IDR : Rp"))
    print ("----------------------------------------")
    idr_usd = pilih / kurs # formula untuk konversi IDR-USD adalah dengan menggunakan pembagian
    print (f"NILAI IDR DALAM USD ADALAH : ${idr_usd:.2f}") # f-string saya gunakan untuk mengubah format value agar desimal dibatasi sebanyak 2 karakter
    print ("----------------------------------------")
elif pilih == 2: # jika memilih 2, maka akan masuk ke menu konversi USD-IDR
    pilih = float(input("MASUKKAN JUMLAH UANG DALAM USD : $"))
    print ("----------------------------------------")
    usd_idr = pilih * kurs # gunakan perkalian untuk mencari nilai USD-IDR
    print (f"NILAI USD DALAM IDR ADALAH : Rp{usd_idr:,.2f}") # saya menggunakan f-string agar dapat memisahkan value yang berjumlah ribuan
    print ("----------------------------------------")
else:
    print ("PILIHAN TIDAK VALID")
    print ("----------------------------------------")
    
## credit and disclaimer

print ("Program ini dikembangkan oleh :")
print ("Rasya Pramudya Teja - 2025310027\n")

# program ini dikembangkan sendiri dengan bantuan :
# kurs dilihat melalui google
# perintah yang digunakan dalam syntax merupakan perintah yang sesuai dengan materi pertemuan 3
# f-string saya pelajari melalui website w3schools.com
