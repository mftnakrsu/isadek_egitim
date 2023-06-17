import os

# Dosyayı Okuma
dosya = open("dosya.txt", "r")
icerik = dosya.read()
print("Dosya içeriği:\n", icerik)
dosya.close()

# Dosyaya Yazma
dosya = open("dosya.txt", "w")
dosya.write("Merhaba, dosyaya yazıyoruz!")
dosya.close()

# Dosyaya Satır Satır Yazma
satirlar = ["Bu birinci satır.", "Bu ikinci satır.", "Bu üçüncü satır."]
dosya = open("dosya.txt", "w")
for satir in satirlar:
    dosya.write(satir + "\n")
dosya.close()

# Dosyayı Append Modunda Güncelleme
dosya = open("dosya.txt", "a")
dosya.write("Bu yeni bir satır.")
dosya.close()

# Dosya Var mı Kontrolü
dosya_adi = "dosya.txt"
if os.path.exists(dosya_adi):
    print("Dosya mevcut.")
else:
    print("Dosya mevcut değil.")
