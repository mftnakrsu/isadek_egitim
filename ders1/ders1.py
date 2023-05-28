#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 28 17:46:12 2023

@author: mef
"""

# VERİ YAPILARI (DATA STRUCTURES)

# Sayılar: integer
x = 46
type(x)

# Sayılar: float
x = 10.3
type(x)

# Sayılar: complex
x = 2j + 1
type(x)

# String
x = "Hello  world"
type(x)

# Boolean
True
False
type(True)
5 == 4
3 == 2
1 == 1


# Liste
x = ["jasmy", "btc", "eth"]
type(x)

# Sözlük (dictionary)
x = {"name": "Peter", "Age": 36}
type(x)

# Tuple
x = ("python", "ml", "ds")
type(x)


type(x)


# Sayılar (Numbers): int, float, complex
###############################################

a = 5
b = 10.5

a * 3
a / 7
a * b / 10
a ** 2


# Tipleri değiştirmek
#######################

int(b)
float(a)

int(a * b / 10)

c = a * b / 10

int(c)

type(10.)

abs(-2) # mutlak deger


liste = [882388, 260409, 72923, 692476, 131925, 259114, 47630, 84513, 25413, 614654,
239479, 299159, 175488, 345972, 458112, 791030, 243610, 413702, 565285,
773607, 131583, 979177, 247202, 615485, 647512, 556823, 242460, 852928,
893126, 792435, 273904, 544434, 627222, 601984, 966446, 384143, 308858,
915106, 914423, 826315, 258342, 188056, 934954, 253918, 468223, 262875,
462902, 370061, 336521, 367829, 147846, 838385, 605377, 175140, 957437]
    
max(sayılar) # maksimumu bulur
min(sayılar) # minimumu bulur


# Karakter Dizileri (Strings)
###############################################

print("John")
print('John')

name = "John"
name = 'John'

nesne = "karakter dizisi"


# Çok Satırlı Karakter Dizileri
#######################


long_str = """Veri Yapıları: Hızlı Özet, 
Sayılar (Numbers): int, float, complex, 
Karakter Dizileri (Strings): str, 
List, Dictionary, Tuple, Set, 
Boolean (TRUE-FALSE): bool"""


# key-value

dictionary = {"araba":"surmeye yarar",
              "bardak": "su icmeye yarar",
              "bilgilerim": ["meftun","akarsu",45]}




"""
BU SCRIPT ARITMATIK ISLEMLERI OGRENIYORUZ
"""
# BU SCRIPT ARITMATIK ISLEMLERI OGRENIYORUZ

sayi1 = 5
sayi2 = 10
ondalik_sayi = 7.0

# print("sayılarım")
# print(sayi1)
# print(sayi2)

"""
print("sayılarım",sayi1,sayi2)

print(1+2)
print(type(1+2))

print(sayi1+sayi2)
print(type(sayi1+sayi2))
"""

# toplam = 1+2
# toplam = sayi1+sayi2
# print(toplam)
# print(type(toplam))

# carpim = sayi1*sayi2
# print(carpim)
# print(type(carpim))

# print(ondalik_sayi)
# #7.0+5
# toplam2=ondalik_sayi+sayi1
# print(toplam2)
# print(type(toplam2))

# cikarma = sayi2-sayi1
# print(cikarma)
# cikarma = sayi1 -sayi2
# print(type(cikarma))
# degisken tanımlama kuralları var, en basa sayi gelemez 2degisken -> degisken2

# bölme işlemi

yeni_sayi = 20
ikinciYeniSayi = 3
Ucuncusayi = 4

print(yeni_sayi/Ucuncusayi)  # 5.0
print(yeni_sayi/ikinciYeniSayi)  # 6.6

bolme_islemim = yeni_sayi/Ucuncusayi  # 5.0
bolme_islemim_2 = yeni_sayi/ikinciYeniSayi  # 6.6


# mod islemleri, %
print(yeni_sayi % Ucuncusayi)  # 20%4
print(yeni_sayi % ikinciYeniSayi)  # 20%3

# == # esit midi, dogru mudur ?


print(2 == 2)
print(type("meftun" == "akarsu"))

durum = "meftun" == "akarsu"
print(durum)
print(type(durum))

# SÖZLÜKLER , dictionary

# (key, value) --> item

sozluk1 = {"bardak" : "kahve icmeye yarar",
           "kalem" : "yazmaya yarar",
           "telefon" : "konusmaya yarar",
           "adim" : "meftun",
           "bilgilerim": ["meftun akarsu"],
           "renkler":["kımrıız,mavi"]}

print(sozluk1)

sayi1 = 5

print(sayi1 == 5)


print("sayi1" == 5)


liste = ["Ahmet", "Mehmet", 23, 65, 3.2]
liste = ["Ali", "Veli", ["Ayşe", "Nazan", "Zeynep"], 34, 65, 33, 5.6]


diller = ["İngilizce", "Fransızca", "Türkçe", "İtalyanca", "İspanyolca"]
len(diller)


meyveler = ["elma", "armut", "çilek", "kiraz"]






