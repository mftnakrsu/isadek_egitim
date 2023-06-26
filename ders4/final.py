def metin_isteme():
    """
    Kullanıcıdan metin girişi alır ve metni döndürür.
    """
    metin = input("Bir metin girin: ")
    return metin

def kelime_sayma(metin):
    """
    Bir metindeki kelime sayısını hesaplar ve döndürür.
    """
    kelimeler = metin.split()
    return len(kelimeler)

def karakter_sayma(metin):
    """
    Bir metindeki karakter sayısını hesaplar ve döndürür.
    """
    return len(metin)

def en_uzun_kelime(metin):
    """
    Bir metindeki en uzun kelimeyi bulur ve döndürür.
    """
    kelimeler = metin.split()
    en_uzun = max(kelimeler, key=len)
    return en_uzun

def en_kisa_kelime(metin):
    """
    Bir metindeki en kısa kelimeyi bulur ve döndürür.
    """
    kelimeler = metin.split()
    en_kisa = min(kelimeler, key=len)
    return en_kisa

def kelimeleri_sirala(metin):
    """
    Bir metindeki kelimeleri alfabetik sıraya göre sıralar ve döndürür.
    """
    kelimeler = metin.split()
    kelimeler.sort()
    return kelimeler

def sonuclari_dosyaya_yazma(dosya_adi, sonuclar):
    """
    Elde edilen sonuçları belirtilen dosyaya güzel bir şekilde yazma işlemini gerçekleştirir.
    """
    with open(dosya_adi, "w") as dosya:
        dosya.write("Metin Analizi Sonuçları:\n")
        dosya.write("========================\n\n")
        dosya.write("Metin: {}\n".format(sonuclar["metin"]))
        dosya.write("Kelime Sayısı: {}\n".format(sonuclar["kelime_sayisi"]))
        dosya.write("Karakter Sayısı: {}\n".format(sonuclar["karakter_sayisi"]))
        dosya.write("En Uzun Kelime: {}\n".format(sonuclar["en_uzun_kelime"]))
        dosya.write("En Kısa Kelime: {}\n".format(sonuclar["en_kisa_kelime"]))
        dosya.write("Sıralanmış Kelimeler:\n")
        for kelime in sonuclar["siralanan_kelimeler"]:
            dosya.write("- {}\n".format(kelime))

def sonuclari_dosyadan_okuma(dosya_adi):
    """
    Belirtilen dosyadan sonuçları okuyarak ekrana yazdırır.
    """
    with open(dosya_adi, "r") as dosya:
        icerik = dosya.read()
    print(icerik)

def metin_analizi_projesi():
    """
    Metin analizi projesini yürütür.
    """
    # Kullanıcıdan metin girişi al
    metin = metin_isteme()

    # Sonuçları hesapla
    sonuclar = {}
    sonuclar["metin"] = metin
    sonuclar["kelime_sayisi"] = kelime_sayma(metin)
    sonuclar["karakter_sayisi"] = karakter_sayma(metin)
    sonuclar["en_uzun_kelime"] = en_uzun_kelime(metin)
    sonuclar["en_kisa_kelime"] = en_kisa_kelime(metin)
    sonuclar["siralanan_kelimeler"] = kelimeleri_sirala(metin)

    # Sonuçları dosyaya yaz
    dosya_adi = "metin_analizi_sonuclar.txt"
    sonuclari_dosyaya_yazma(dosya_adi, sonuclar)
    print("Sonuçlar dosyaya yazıldı: {}".format(dosya_adi))

    # Dosyadan sonuçları oku ve ekrana yazdır
    sonuclari_dosyadan_okuma(dosya_adi)

# Metin analizi projesini çalıştır
metin_analizi_projesi()
