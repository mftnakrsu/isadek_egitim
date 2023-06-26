def kullanici_girisi():
    dogru_kullanici_adi = "admin"
    dogru_sifre = "123456"
    giris_hakki = 3

    while giris_hakki > 0:
        kullanici_adi = input("Kullanıcı adınızı girin (q: Çıkış): ")
        
        if kullanici_adi.lower() == "q":
            return False

        sifre = input("Şifrenizi girin (q: Çıkış): ")

        if sifre.lower() == "q":
            return False

        if kullanici_adi != dogru_kullanici_adi and sifre != dogru_sifre:
            print("Hatalı kullanıcı adı ve şifre.")
        elif kullanici_adi != dogru_kullanici_adi:
            print("Hatalı kullanıcı adı.")
        elif sifre != dogru_sifre:
            print("Hatalı şifre.")
        else:
            print("Giriş başarılı.")
            return True

        giris_hakki -= 1
        print("Kalan giriş hakkınız:", giris_hakki)

    print("Giriş hakkınız kalmadı. Hesabınız bloke edildi.")
    return False


def sifre_yenileme():
    dogru_sifre = "123456"
    giris_hakki = 3

    while giris_hakki > 0:
        girilen_sifre = input("Mevcut şifrenizi girin (q: Çıkış): ")
        
        if girilen_sifre.lower() == "q":
            return False

        if girilen_sifre == dogru_sifre:
            yeni_sifre = input("Yeni şifreyi girin (q: Çıkış): ")
            
            if yeni_sifre.lower() == "q":
                return False

            dogrulama_sifre = input("Yeni şifreyi doğrulayın (q: Çıkış): ")
            
            if dogrulama_sifre.lower() == "q":
                return False

            if yeni_sifre == dogrulama_sifre:
                dogru_sifre = yeni_sifre
                print("Şifre başarıyla güncellendi.")
                return True
            else:
                print("Şifreler eşleşmiyor. Lütfen tekrar deneyin.")
        else:
            giris_hakki -= 1
            print("Mevcut şifre hatalı. Kalan giriş hakkınız:", giris_hakki)

    print("Giriş hakkınız kalmadı. Şifre yenileme işlemi başarısız.")
    return False


def hesap_olusturma():
    hesaplar = []

    while True:
        kullanici_adi = input("Kullanıcı adınızı girin (q: Çıkış): ")

        if kullanici_adi.lower() == "q":
            return False

        if not kullanici_adi:
            print("Kullanıcı adı boş olamaz. Lütfen tekrar deneyin.")
            continue

        if kullanici_adi in hesaplar:
            print("Bu kullanıcı adı zaten kullanılıyor. Lütfen farklı bir kullanıcı adı seçin.")
        else:
            hesaplar.append(kullanici_adi)
            print("Hesap oluşturuldu.")
            return True


def kullanici_yetkilendirme():
    yetkili_kullanicilar = ["admin", "moderator"]
    giris_hakki = 3

    while giris_hakki > 0:
        kullanici_adi = input("Kullanıcı adınızı girin (q: Çıkış): ")
        
        if kullanici_adi.lower() == "q":
            return False

        if kullanici_adi in yetkili_kullanicilar:
            print("Yetkili kullanıcı girişi başarılı.")
            return True
        else:
            giris_hakki -= 1
            print("Yetkisiz kullanıcı. Kalan giriş hakkınız:", giris_hakki)

    print("Giriş hakkınız kalmadı. Yetkilendirme başarısız.")
    return False


# Ana program akışı
while True:
    print("1. Kullanıcı Girişi")
    print("2. Şifre Yenileme")
    print("3. Hesap Oluşturma")
    print("4. Kullanıcı Yetkilendirme")
    print("5. Çıkış")
    secim = input("İşlem seçin (1-5): ")

    if secim == "1":
        if not kullanici_girisi():
            break
    elif secim == "2":
        if not sifre_yenileme():
            break
    elif secim == "3":
        if not hesap_olusturma():
            break
    elif secim == "4":
        if not kullanici_yetkilendirme():
            break
    elif secim == "5":
        print("Program sonlandırılıyor.")
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")
