# -*- coding: utf-8 -*-


# Koşul durumları
# if else ifadeleri
# Örnek ifadeler
# Döngüler
# For/ while ifadeleri

# Problem tanımı : Yaşım 18, ehliyet alamıyorum.
# EGER , DURUM
    # SONUC
# IF kosul doğru
# ELSE



yas =  int(input("Yasınzı giriniz: "))
yas=int(yas)

if yas >= 18:
    print("Ehliyet alabilirsiniz.")
else:
    print("Ehliyet alamazsınız")
    

# Sayı isteyeceğim, bu sayı 0'dan büyük mü deği mi ?
# 0'dan büyükse , 0dan büyük yazsın
# Diğer koşuldada 0dan Büyük değil yazsın
# Sayı 0'a eşitse sayı 0'a eşitttir

sayi = input("sayi giriniz") 
sayi = int(sayi)

if sayi > 0:
    print("Sayı 0'dan büyük")
    
elif sayi == 0 :
    print("Sayi 0'a eşittir")
    
else:
    print("sayı 0dan küçük")


# Problem tanımım : Üniversite sınav notunu al, input, float
# 90'dan büyükse --> AA
# 80'den büyükse BA
# 70'den büyükse BB
# 60'dan büyükse CB
# Else FF

"""
If (Koşul):
    Sonuç1 
Else:
    Sonuç2
"""

notum = input("Not giriniz")
notum = float(notum)

if notum>100:
    print("Notunuz 100den büyük olamaz")

else:
    
    if notum>=90:
        print("Notum AA")
    elif notum>80:
        print("Notum BA")
    elif notum>=70:
        print("BB")
    elif notum>=60:
        print("Notum CB")
    else:
        print("Notum FF")

# Problem tanımı 
# Sayı 10dan büyükse 10dan büyük 
# 0 - 10 arasındaysa , 0-10 arasında yazdın
# 0'a eşitse 0a eşit yazsın
# 0'dan küçükse de 0'dan küçk yazsın

yeni_sayi = input("Sayi giriniz")

if type(yeni_sayi) == str or type(yeni_sayi)==float:
    print("Girilen değer string veya float olmamalı.")
    
else:
    
    if yeni_sayi>10:
        print("10dan büyük ")
    elif yeni_sayi>0 and yeni_sayi<10:
        print("0 - 10 arasında")
    elif yeni_sayi == 0:
        print("0'a eşittir")
    else:
        print("0dan küçüktür")
        
        
# Problem tanımı
# hava durumunu alsın kapalı açık

hava_durumu = []
hava_durumu.append("ACIK")
hava_durumu.append("KAPALI")

hava_acık = hava_durumu[0]
hava_kapalı =hava_durumu[1]

guncel_hava_durumu=input("Hava durumu giriniz:")

if guncel_hava_durumu == "ACIK":
    print("Kısakolu giy")
    
elif guncel_hava_durumu =="KAPALI":
    print("Hava kaplaı, kapaplı giyin")
else:
    print("Hava  belirsiz")

# giriş uygulama


yasim =18
if yasim>18:
    print("yasim 18den büykü ehliyet alabirim")
elif yasim == 18:
    print("yasım 18, ayrıca ehliyet alabilirim.")
else:
    print("ehliyet alamam")
        

