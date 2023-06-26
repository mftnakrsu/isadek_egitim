##### ÖRNEK 1 #####
def kelime_ters_cevir(kelime):
    ters_kelime = ""
    for harf in kelime:
        ters_kelime = harf + ters_kelime
    return ters_kelime

def kelime_isle():
    kelime = input("Kelime veya cümle girin: ")
    ters_kelime = kelime_ters_cevir(kelime)
    print("Ters çevrilmiş hali:", ters_kelime)

kelime_isle()


def kelime_ters_cevir():
    kelime = input("Kelime veya cümle girin: ")
    ters_kelime = kelime[::-1]
    return ters_kelime

def kelime_isle():
    ters_kelime = kelime_ters_cevir()
    print("Ters çevrilmiş hali:", ters_kelime)
    # Ters çevrilmiş kelimeyi başka işlemlerde kullanabilirsiniz.
    # Örneğin, ters_kelimeyi bir dosyaya yazabilirsiniz.

kelime_isle()
