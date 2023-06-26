def satir_satir_girdi():
    with open("metin.txt", "w") as dosya:
        while True:
            satir = input("Bir satır girin ('q' girerek çıkış yapın): ")
            if satir == "q":
                break
            dosya.write(satir + "\n")
            
satir_satir_girdi()