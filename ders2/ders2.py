# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 08:39:54 2023

@author: AMK3BU
"""
# 01.06.2023 Toplantı notları


# ÖDEV1
sayi1 = 10.1
sayi2 = 4
sayi3 = 1
print(sayi1*sayi2*sayi3)

# ÖDEV2 
boy = 192 # cm
kilom = 94 # kg
bki = kilom/boy

print("beden kütle indeksim",bki)

# ÖDEV 4
print("meftun")
print("akarsu")

print("meftun","\n","akarsu")
print("meftun","\t","akarsu")

ad =  "zeynep"
soyad = "kalkan"
numara = "0540983409"

print("Adım: ",ad,"\n","Soyadım:",soyad,"\n","Numaram: ",numara)

# SORU 5
ucgenin_birinci_kenarı = 3 # cm
ucgenın_ikinci_kenarı  = 4 # cm

hipotenus = ucgenin_birinci_kenarı**2 + ucgenın_ikinci_kenarı**2
print("Hipotenus",hipotenus)
hipotenus = hipotenus ** 0.5
print("Hipotenus",hipotenus)

# TIP DONUSUMLARI
# float int

print(type(hipotenus))
# float - int 
hipotenus = int(hipotenus)

print("Hipotenus", hipotenus," Tipi", type(hipotenus))

numaram = 74837438748
print("numaram:", numaram, type(numaram))

# int - str
numaram = str(numaram)
print(type(numaram))

hava_acik_mi = True
print(type(hava_acik_mi))

hava_acik_mi = str(hava_acik_mi)
print(type(hava_acik_mi))

# INPUT fonksiyonu
# degisken = input ("")

# adım = input("Adınızı giriniz: ")
# print("Adım:", adım)

# soyadım = input("Soyadıınızı giriniz: ")
# print("Soyadım:", soyadım)

#yasim = input("Yasınızı giriniz: ") # default , varsayılanı str
#yasim = int(yasim)

#print("Yasımın iki katı", yasim*2)

# KARAKTER DİZİLERİ , LİSTE METHODLARI
liste1 = ["meftun","akarsu",26,"bartın","bardak","istanbul"] # 0 - 1 - 2 - 3

adım = liste1[0]
memleketim = liste1[3]
print("memleketim", memleketim)

deneme = liste1[-2]
print(deneme)

# listeye eleman ekleme
meyveler = []
meyveler.append("elma")

print(meyveler)

# BİLGİLER
bilgiler = []
print(bilgiler)
# adımı, input, soyadımı input, yasımı input, apppend
yas = input("Yas giriniz(int)") # INPUT HER ZAMAN STRING GELIYOR
yas = int(yas)
print(type(yas))

adım_degiskeni = input("Adınızı giriniz:")
soyadım_degiskeni = input("Soyad giriniz")

bilgiler.append(soyadım_degiskeni)
bilgiler.append(yas)
bilgiler.append(adım_degiskeni)

print(bilgiler)





    



