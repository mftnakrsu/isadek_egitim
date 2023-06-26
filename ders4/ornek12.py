def palindromik_mi(sayi):
    """
    Bir sayının palindromik olup olmadığını kontrol eder.

    Parameters:
        sayi (int): Kontrol edilecek sayı.

    Returns:
        bool: Eğer sayı palindromik ise True, değilse False döner.
    """
    # Sayıyı string olarak dönüştürüyoruz ve ters çevirerek kontrol ediyoruz
    if str(sayi) == str(sayi)[::-1]:
        return True
    else:
        return False

# Kullanıcıdan bir sayı istiyoruz
sayi = int(input("Bir sayı girin: "))

# Palindromik kontrolünü yaparak sonucu ekrana yazdırıyoruz
if palindromik_mi(sayi):
    print(f"{sayi} palindromik bir sayıdır.")
else:
    print(f"{sayi} palindromik bir sayı değildir.")
