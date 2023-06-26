"""
Örneğin, "listen" kelimesini ele alalım. 
Bu kelimenin harflerini yerlerini değiştirerek "silent" kelimesini 
elde edebiliriz. İki kelime aynı harfleri içerdiği için ve harflerin 
sıraları değiştirilerek birbirine dönüştürülebildiği için "listen" 
ve "silent" birbirinin anagramıdır.

Anagramlar genellikle bir kelimenin veya cümlenin harflerini
 karıştırarak başka bir kelime veya cümle oluşturmanın yanı sıra,
 daha geniş kapsamlı olabilir. Örneğin, "cinema" kelimesi ile "iceman" 
 kelimesi de birbirinin anagramıdır.

Anagramlar, dilbilgisi kurallarına veya anlam içeriğine bakmaksızın,
 sadece harf kombinasyonlarına odaklanır. Bu nedenle, aynı harfleri 
 içeren farklı kelimeler veya kelime grupları anagram olabilir.

"""

def anagram_mi(s1, s2):
    return sorted(s1) == sorted(s2)

kelime1 = input("Birinci kelimeyi girin: ")
kelime2 = input("Ikinci kelimeyi girin: ")

if anagram_mi(kelime1, kelime2):
    print(f"{kelime1} ve {kelime2} birbirinin anagramıdır.")
else:
    print(f"{kelime1} ve {kelime2} birbirinin anagramı değildir.")



