angka = input("Masukkan angka : ")
hitung = input("Masukkan angka yang dihitung: ")

a = 0

for i in angka:
    if hitung in i:
        a +=1

print("angka",hitung,"muncul sebanyak",a,"kali")