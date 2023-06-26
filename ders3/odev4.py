def kullanici_adini_al():
    kullanici_adi = input("Kullanıcı adınızı belirleyin: ")
    while len(kullanici_adi) > 40:
        print("Kullanıcı adı 40 karakteri geçemez!")
        kullanici_adi = input("Kullanıcı adınızı tekrar belirleyin: ")
    return kullanici_adi


def parolayi_al():
    parola = input("Parolanızı belirleyin: ")
    while len(parola) > 40:
        print("Parola 40 karakteri geçemez!")
        parola = input("Parolanızı tekrar belirleyin: ")
    return parola


kullanici_adi = kullanici_adini_al()
parola = parolayi_al()

print("Kullanıcı adı:", kullanici_adi)
print("Parola:", parola)
