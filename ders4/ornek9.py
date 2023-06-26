def kelime_sayisi(metin):
    kelimeler = metin.lower().split()
    kelime_sayilari = {}

    for kelime in kelimeler:
        if kelime in kelime_sayilari:
            kelime_sayilari[kelime] += 1
        else:
            kelime_sayilari[kelime] = 1

    return kelime_sayilari

metin = """
Bu bir deneme metnidir. Bu metin içinde bazı bazı tekrarlayan kelimeler bulunmaktadır.
Bazı bazı kelimeler tekrar tekrar geçmektedir. Bu metindeki kelimelerin sayılarını bulalım.
"""

kelime_sayilari = kelime_sayisi(metin)
for kelime, sayi in kelime_sayilari.items():
    print(f"{kelime}: {sayi}")
