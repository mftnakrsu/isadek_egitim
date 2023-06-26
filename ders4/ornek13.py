def kelime_sayma(metin):
    """
    Bir metindeki kelime sayısını hesaplar.

    Parameters:
        metin (str): Kelime sayısı hesaplanacak metin.

    Returns:
        int: Metindeki kelime sayısı.
    """
    kelimeler = metin.split()
    return len(kelimeler)

# Kullanıcıdan metin girişi alıyoruz
metin = input("Bir metin girin: ")

# Metindeki kelime sayısını hesaplıyoruz
kelime_sayisi = kelime_sayma(metin)

# Sonucu ekrana yazdırıyoruz
print("Metindeki kelime sayısı:", kelime_sayisi)
