# -*- coding: utf-8 -*-

# for, while
# DONGULER FOR
# FOR KOSUL:
    # SONUÇ

meyve1= meyveler[0]
meyve2= meyveler[1]
meyve3= meyveler[2]
meyve4= meyveler[-1]

print("1. meyve:",meyve1)
print("2. meyve:",meyve2)
print("3. meyve:",meyve3)
print("4. meyve:",meyve4)
    
meyveler = ["elma","armut","karpuz","kiraz","meyve"]

sayilar = [1,2,3,4,5,6,7,8,9,10]
for i in sayilar:
    if i%2==0:
        print(i,"sayısı çifttir")
    else:
        print(i,"sayısı tektir")

range(baslangıc_degeri,bitis degeri,atlama degeri)

yeni_sayilar= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for a in range(0, 1000):
    if a%2==0:
        print(a,"sayısı çifttir.")

# LEN Fonksiyonu --> uzunluk
# len()

# PROBLEM: Listemin uzunlugu 100
for i in yeni_sayilar:
    print(i)

for i in range(1,21):
    print(i)
 
    
# kullanııcıdan 1-2000 arasında sayı alsın,
# Kullanıcı hangi sayıyı girdiyse, o sayıya kadarkı 5in katlarını alsın

sayi = input("0-2000 arasında bir sayi giriniz")
sayi = int(sayi)

for i in range(0,sayi):
    if i%5==0:
        print(i,"sayısı 5e bölünür")
    else:
        print(i,"sayısı 5e bölünmez")
        
for i in range(0,sayi,5):
    print(i)