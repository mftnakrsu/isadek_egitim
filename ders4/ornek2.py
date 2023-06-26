def kullanici_girisi():
    dogru_kullanici_adi = "admin"
    dogru_sifre = "123456"
    giris_hakki = 3

    while giris_hakki > 0:
        kullanici_adi = input("Kullanıcı adınızı girin: ")
        sifre = input("Şifrenizi girin: ")

        if kullanici_adi != dogru_kullanici_adi and sifre != dogru_sifre:
            print("Kullanıcı adı ve şifre yanlış.")
        elif kullanici_adi != dogru_kullanici_adi:
            print("Kullanıcı adı yanlış.")
        elif sifre != dogru_sifre:
            print("Şifre yanlış.")
        else:
            print("Giriş başarılı.")
            break

        giris_hakki -= 1
        print("Kalan giriş hakkınız:", giris_hakki)

        if giris_hakki == 0:
            print("Giriş hakkınız kalmadı. Hesabınız bloke edildi.")
            return

kullanici_girisi()
