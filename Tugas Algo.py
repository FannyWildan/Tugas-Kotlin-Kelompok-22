angka = int(input("Masukan angka: "))

hasil = angka % 2

if angka < 15:
    if hasil == 0:
        print ("Bilangan Genap dan angka kecil")
    else :
        print("Bilangan Ganjil dan angka kecil")
elif 15 <= angka <= 40:
    if hasil == 0:
        print ("Bilangan Genap dan angka sedang")
    else :
        print ("Bilangan Ganjil dan angka sedang")
else:
    if hasil == 0:
        print ("Bilangan Genap dan angka besar")
    else :
        print("Bilangan Ganjil dan angka besar")

