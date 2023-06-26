#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 09:37:40 2023

@author: mef
"""

# ÇÖZÜM 1 #

while True:
    print("İşlem Seçenekleri:")
    print("(1) Topla")
    print("(2) Çıkar")
    print("(3) Çarp")
    print("(4) Böl")
    print("(5) Karesini Hesapla")
    print("(6) Karekök Hesapla")
    print("Çıkmak için q ya basınız")

    secim = input("Yapmak istediğiniz işlemi seçin (1-6): ")

    sayi1 = float(input("Toplama işlemi için ilk sayıyı girin: "))
    sayi2 = float(input("Toplama işlemi için ikinci sayıyı girin: "))
     
    if secim == "1":
       
        sonuc = sayi1 + sayi2
        print("SONUC: ", sonuc)
    elif secim == "2":
        
        sonuc = sayi1 - sayi2
        print("SONUC: ", sonuc)
    elif secim == "3":
      
        sonuc = sayi1 * sayi2
        print("SONUC: ", sonuc)
    elif secim == "4":

        if sayi2 != 0:
            sonuc = sayi1 / sayi2
            print("SONUC: ", sonuc)
        else:
            print("Hata! İkinci sayı sıfır olamaz.")
    elif secim == "5":
        sayi = float(input("Karesini hesaplamak istediğiniz sayıyı girin: "))
        sonuc = sayi ** 2
        print("SONUC: ", sonuc)
    elif secim == "6":
        sayi = float(input("Karekökünü hesaplamak istediğiniz sayıyı girin: "))
        sonuc = sayi ** 0.5
        print("SONUC: ", sonuc)
    elif secim.lower() == "esc":
        print("Hesap makinesi kapatılıyor...")
        break
    else:
        print("Geçersiz bir seçenek girdiniz. Lütfen tekrar deneyin.")
        

# ÇÖZÜM 2 #


def topla():
    sayi1 = float(input("Toplama işlemi için ilk sayıyı girin: "))
    sayi2 = float(input("Toplama işlemi için ikinci sayıyı girin: "))
    sonuc = sayi1 + sayi2
    print("Sonuç: ", sonuc)

def cikar():
    sayi1 = float(input("Çıkarma işlemi için ilk sayıyı girin: "))
    sayi2 = float(input("Çıkarma işlemi için ikinci sayıyı girin: "))
    sonuc = sayi1 - sayi2
    print("Sonuç: ", sonuc)

def carp():
    sayi1 = float(input("Çarpma işlemi için ilk sayıyı girin: "))
    sayi2 = float(input("Çarpma işlemi için ikinci sayıyı girin: "))
    sonuc = sayi1 * sayi2
    print("Sonuç: ", sonuc)

def bol():
    sayi1 = float(input("Bölme işlemi için ilk sayıyı girin: "))
    sayi2 = float(input("Bölme işlemi için ikinci sayıyı girin: "))
    if sayi2 != 0:
        sonuc = sayi1 / sayi2
        print("Sonuç: ", sonuc)
    else:
        print("Hata! İkinci sayı sıfır olamaz.")

def karesini_hesapla():
    sayi = float(input("Karesini hesaplamak istediğiniz sayıyı girin: "))
    sonuc = sayi ** 2
    print("Sonuç: ", sonuc)

def karekok_hesapla():
    sayi = float(input("Karekökünü hesaplamak istediğiniz sayıyı girin: "))
    sonuc = sayi ** 0.5
    print("Sonuç: ", sonuc)

def hesap_makinesi():
    while True:
        print("İşlem Seçenekleri:")
        print("(1) Topla")
        print("(2) Çıkar")
        print("(3) Çarp")
        print("(4) Böl")
        print("(5) Karesini Hesapla")
        print("(6) Karekök Hesapla")

        secim = input("Yapmak istediğiniz işlemi seçin (1-6): ")

        if secim == "1":
            topla()
        elif secim == "2":
            cikar()
        elif secim == "3":
            carp()
        elif secim == "4":
            bol()
        elif secim == "5":
            karesini_hesapla()
        elif secim == "6":
            karekok_hesapla()
        elif secim.lower() == "q":
            print("Hesap makinesi kapatılıyor...")
            break
        else:
            print("Geçersiz bir seçenek girdiniz. Lütfen tekrar deneyin.")
            
            
            
# ODEV 3 #

import msvcrt

def topla():
    sayi1 = float(input("Toplama işlemi için ilk sayıyı girin: "))
    sayi2 = float(input("Toplama işlemi için ikinci sayıyı girin: "))
    sonuc = sayi1 + sayi2
    return sonuc

def cikar():
    sayi1 = float(input("Çıkarma işlemi için ilk sayıyı girin: "))
    sayi2 = float(input("Çıkarma işlemi için ikinci sayıyı girin: "))
    sonuc = sayi1 - sayi2
    return sonuc

def carp():
    sayi1 = float(input("Çarpma işlemi için ilk sayıyı girin: "))
    sayi2 = float(input("Çarpma işlemi için ikinci sayıyı girin: "))
    sonuc = sayi1 * sayi2
    return sonuc

def bol():
    sayi1 = float(input("Bölme işlemi için ilk sayıyı girin: "))
    sayi2 = float(input("Bölme işlemi için ikinci sayıyı girin: "))
    if sayi2 != 0:
        sonuc = sayi1 / sayi2
        return sonuc
    else:
        print("Hata! İkinci sayı sıfır olamaz.")

def karesini_hesapla():
    sayi = float(input("Karesini hesaplamak istediğiniz sayıyı girin: "))
    sonuc = sayi ** 2
    return sonuc

def karekok_hesapla():
    sayi = float(input("Karekökünü hesaplamak istediğiniz sayıyı girin: "))
    sonuc = sayi ** 0.5
    return sonuc

def hesap_makinesi():
    while True:
        print("İşlem Seçenekleri:")
        print("(1) Topla")
        print("(2) Çıkar")
        print("(3) Çarp")
        print("(4) Böl")
        print("(5) Karesini Hesapla")
        print("(6) Karekök Hesapla")

        secim = input("Yapmak istediğiniz işlemi seçin (1-6): ")

        if secim == "1":
            sonuc = topla()
            print("Sonuç: ", sonuc)
        elif secim == "2":
            sonuc = cikar()
            print("Sonuç: ", sonuc)
        elif secim == "3":
            sonuc = carp()
            print("Sonuç: ", sonuc)
        elif secim == "4":
            sonuc = bol()
            if sonuc is not None:
                print("Sonuç: ", sonuc)
        elif secim == "5":
            sonuc = karesini_hesapla()
            print("Sonuç: ", sonuc)
        elif secim == "6":
            sonuc = karekok_hesapla()
            print("Sonuç: ", sonuc)
        elif secim.lower() == "q":
            print("Hesap makinesi kapatılıyor...")
            break
        else:
            print("Geçersiz bir seçenek girdiniz. Lütfen tekrar deneyin.")

        if msvcrt.kbhit() and ord(msvcrt.getch()) == 27:  # ESC tuşuna basılıp basılmadığını kontrol eder
            print("Hesap makinesi kapatılıyor...")
            break

hesap_makinesi()


