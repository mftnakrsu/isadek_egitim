import random

def random_sayi_oyunu():
    sayi = random.randint(1, 100)
    deneme_sayisi = 4
    
    print("1 ile 100 arasında bir sayıyı tahmin et. Toplam 4 denemen var.")
    
    while deneme_sayisi > 0:
        tahmin = int(input("Tahminin: "))
        
        if tahmin == sayi:
            print("Tebrikler! Doğru tahmin ettin.")
            return
        
        if tahmin < sayi:
            print("Daha büyük bir sayı dene.")
        else:
            print("Daha küçük bir sayı dene.")
            
        deneme_sayisi -= 1
        print(f"Kalan deneme hakkın: {deneme_sayisi}")
    
    print("Maalesef, deneme hakkını doldurdun. Oyun bitti.")

random_sayi_oyunu()
