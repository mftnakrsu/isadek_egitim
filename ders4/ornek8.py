def tekrarlayan_kelimeler(text):
    kelimeler = text.lower().split()
    tekrarlayanlar = set()
    tekil_kelimeler = set()

    for kelime in kelimeler:
        if kelime in tekil_kelimeler:
            tekrarlayanlar.add(kelime)
        else:
            tekil_kelimeler.add(kelime)

    return tekrarlayanlar

metin = """Bu bir deneme metnidir.
         Bu metin içinde bazı bazı tekrarlayan 
         kelimeler bulunmaktadır."""

tekrarlayanlar = tekrarlayan_kelimeler(metin)
print("Tekrarlayan kelimeler:", ", ".join(tekrarlayanlar))
