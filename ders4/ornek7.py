def tarih_formati_donustur(tarih):
    gun, ay, yil = tarih.split("/")
    yeni_tarih = ay + "/" + gun + "/" + yil
    return yeni_tarih

def tarih_donustur():
    tarih = input("Tarihi girin (dd/mm/yyyy): ")
    yeni_tarih = tarih_formati_donustur(tarih)
    print("Yeni format:", yeni_tarih)

tarih_donustur()
