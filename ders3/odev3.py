kelime_sozlugu = {}

dosya = open("seyahatin_onemi.txt", "r")
icerik = dosya.read()
dosya.close()

kelimeler = icerik.split()
for kelime in kelimeler:
    if kelime in kelime_sozlugu:
        kelime_sozlugu[kelime] += 1
    else:
        kelime_sozlugu[kelime] = 1

print("Kelime Sözlüğü:")
for kelime, frekans in kelime_sozlugu.items():
    print(f"{kelime}: {frekans}")
 