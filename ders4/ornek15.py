def dosyadan_okuma(dosya_adi):
    """
    Belirtilen dosyayı okuyarak içeriğini döndürür.

    Parameters:
        dosya_adi (str): Okunacak dosyanın adı.

    Returns:
        str: Dosyanın içeriği.
    """
    with open(dosya_adi, "r") as dosya:
        icerik = dosya.read()
    return icerik

# Kullanıcıdan dosya adı bilgisini alıyoruz
dosya_adi = input("Dosya adını girin: ")

# Dosyadan okuma işlemini gerçekleştiriyoruz
icerik = dosyadan_okuma(dosya_adi)

print("Dosyanın içeriği:")
print(icerik)
