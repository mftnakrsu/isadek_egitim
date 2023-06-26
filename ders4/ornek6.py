"""
Kullanıcıdan bir kelime girmesi istenir.
Girilen kelime kelime değişkenine atanır.
kelime değişkeni, ters çevrilmek üzere ters_kelime değişkenine atılır. Ters çevirme işlemi için [::-1] dilimleme yöntemi kullanılır.
Girilen kelimenin, ters çevrilmiş hali ile aynı olup olmadığı kontrol edilir.
Eğer kelime ve ters_kelime birbirine eşitse, yani girilen kelime palindromik ise:
"Girilen kelime palindromiktir." mesajı ekrana yazdırılır.
Eğer kelime ve ters_kelime birbirine eşit değilse, yani girilen kelime palindromik değilse:
"Girilen kelime palindromik değildir." mesajı ekrana yazdırılır.
İşte bu adımlar, girilen kelimenin palindromik olup olmadığını kontrol eden basit bir programın komut satırlarını açıklar.

"""



def palindrom_kontrol(kelime):
    ters_kelime = kelime[::-1]
    if kelime == ters_kelime:
        return True
    else:
        return False

kelime = input("Bir kelime girin: ")
if palindrom_kontrol(kelime):
    print("Girilen kelime palindromiktir.")
else:
    print("Girilen kelime palindromik değildir.")
