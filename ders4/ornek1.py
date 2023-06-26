def atm():
    # Banka hesap bilgileri
    hesap_bakiyesi = 1000
    dogru_hesap_numarasi = "123456789"
    dogru_sifre = "1234"
    giris_hakki = 3

    while giris_hakki > 0:
        # Kullanıcıdan hesap numarası ve şifre istenir
        girilen_hesap_numarasi = input("Hesap numaranızı girin: ")
        girilen_sifre = input("Şifrenizi girin: ")

        # Hesap numarası ve şifre kontrol edilir
        if girilen_hesap_numarasi == dogru_hesap_numarasi and girilen_sifre == dogru_sifre:
            print("Giriş başarılı.")
            break
        else:
            giris_hakki -= 1
            print("Hesap numarası veya şifre hatalı. Kalan giriş hakkınız:", giris_hakki)

            if giris_hakki == 0:
                print("Giriş hakkınız kalmadı. ATM kartınız bloke edildi.")
                return

    while True:
        # Kullanıcıya işlem seçenekleri gösterilir
        print("1. Bakiye sorgulama")
        print("2. Para çekme")
        print("3. Para yatırma")
        print("4. Çıkış")

        secim = input("Yapmak istediğiniz işlemi seçin: ")

        if secim == "1":
            print("Hesap bakiyeniz:", hesap_bakiyesi)
        elif secim == "2":
            cekilecek_miktar = float(input("Çekmek istediğiniz miktarı girin: "))
            if cekilecek_miktar <= hesap_bakiyesi:
                hesap_bakiyesi -= cekilecek_miktar
                print("Paranız çekildi. Güncel hesap bakiyeniz:", hesap_bakiyesi)
            else:
                print("Yetersiz bakiye.")
        elif secim == "3":
            yatirilan_miktar = float(input("Yatırmak istediğiniz miktarı girin: "))
            hesap_bakiyesi += yatirilan_miktar
            print("Paranız yatırıldı. Güncel hesap bakiyeniz:", hesap_bakiyesi)
        elif secim == "4":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")


atm()
