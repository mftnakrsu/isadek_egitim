def dosyaya_yazma(dosya_adi, metin):
    """
    Bir metni belirtilen dosyaya yazma işlemini gerçekleştirir.

    Parameters:
        dosya_adi (str): Yazılacak dosyanın adı.
        metin (str): Yazılacak metin.

    Returns:
        None
    """
    with open(dosya_adi, "w") as dosya:
        dosya.write(metin)

# Kullanıcıdan dosya adı ve yazılacak metin bilgisini alıyoruz
dosya_adi = input("Dosya adını girin: ")
metin = input("Yazılacak metni girin: ")

# Dosyaya yazma işlemini gerçekleştiriyoruz
dosyaya_yazma(dosya_adi, metin)

print("Dosya yazma işlemi tamamlandı.")
