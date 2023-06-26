def faktoriyel_hesapla(sayi):
    faktoriyel = 1
    for i in range(1, sayi + 1):
        faktoriyel *= i
    return faktoriyel

sayi = int(input("Bir sayı girin: "))
print("Faktöriyel:", faktoriyel_hesapla(sayi))
