import string

ilk_metin = """
    Modüler yapısı, sınıf dizgesini (sistem) ve her türlü veri alanı girişini destekler. Hemen hemen her türlü platformda çalışabilir 
    (Unix, Linux, Mac, Windows, Amiga, Symbian). Python ile sistem programlama, kullanıcı arabirimi programlama, ağ programlama, web 
    programlama, uygulama ve veri tabanı yazılımı programlama gibi birçok alanda yazılım geliştirebilirsiniz. Büyük yazılımların hızlı 
    bir şekilde prototiplerinin üretilmesi ve denenmesi gerektiği durumlarda da C ya da C++ gibi dillere tercih edilir.
"""

ikinci_metin = """
    Python 1980'lerin sonunda ABC programlama diline alternatif olarak tasarlanmıştı. Python 2.0, ilk kez 2000 yılında yayınlandı. 
    2008'de yayınlanan Python 3.0, dilin önceki versiyonuyla tam uyumlu değildir ve Python 2.x'te yazılan kodların Python 3.x'te 
    çalışması için değiştirilmesi gerekmektedir. Python 2 versiyonun resmi geliştirilme süreci, dilin son sürümü olan Python 2.7.x serisi
    versiyonların ardından 1 Ocak 2020 itibarıyla resmi olarak sona erdi. Python 2.x geliştirilme desteğinin sona ermesinin ardından, 
    Python dilinin 3.7.x ve sonraki sürümlerinin geliştirilmesi devam etmektedir.
"""

# Noktalama işaretlerini belirleyelim
noktalama_isaretleri = string.punctuation
print(noktalama_isaretleri)

# Noktalama işaretlerini temizleme fonksiyonu
def noktalama_temizle(metin):
    temiz_metin = ""
    for karakter in metin:
        if karakter not in noktalama_isaretleri:
            temiz_metin += karakter
    return temiz_metin

# Metinleri noktalama işaretlerinden temizleyelim
temiz_ilk_metin = noktalama_temizle(ilk_metin)
temiz_ikinci_metin = noktalama_temizle(ikinci_metin)

# Metinleri küçük harflere dönüştürelim ve kelimelere ayıralım
ilk_metin_kelimeler = temiz_ilk_metin.lower().split()
ikinci_metin_kelimeler = temiz_ikinci_metin.lower().split()

# Ortak kelimeleri bulma
ortak_kelimeler = set(ilk_metin_kelimeler) & set(ikinci_metin_kelimeler)

# Ortak kelimeleri ekrana yazdırma
print("Ortak Kelimeler:")
for kelime in ortak_kelimeler:
    print(kelime)
