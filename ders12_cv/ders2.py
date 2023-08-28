# opencv kütüphanesi cv2

import cv2  # burada opencv kütüphanesini çağırdım

atv_resmi = cv2.imread("/home/mef/Desktop/python_egitimi/atv.jpeg") # resim oku fonksiyonu
print(atv_resmi.shape)

# pencere adi, gösterilecek resim
cv2.imshow("Opencv egitiminin ilk dersinin penceresi", atv_resmi) # image shor, resmi göster

# griye çevirme , conver colour (resim, hangi türe cevirecegiz)
gri_atv_resmi = cv2.cvtColor(atv_resmi, cv2.COLOR_RGB2GRAY)
print(gri_atv_resmi.shape)
cv2.imshow("gri atv resmi",gri_atv_resmi)
# gri resmi renkliye cevir

## hata, reverse işlemi
#griden_renkliye_cevirme = cv2.cvtColor(gri_atv_resmi, cv2.COLOR_GRAY2BGR)
#cv2.imshow("Griden renklisye çevirdigim resim",griden_renkliye_cevirme)

# bulanıklaştırma işlemleri kernel derecesi arttıkça bulanıklaştırma derecesi artıyor
bulanik_resim = cv2.GaussianBlur(atv_resmi, (7,7), cv2.BORDER_DEFAULT)
cv2.imshow("BULANIK ATV RESMI",bulanik_resim)
print(bulanik_resim.shape)


# EDGE DETECTION  # Canny edge detection
kenari_testip_edilen_resim = cv2.Canny(bulanik_resim, 100, 175)
cv2.imshow("kenari tespit ettim", kenari_testip_edilen_resim)

# DILATE ISLEMİ 
# resim ,kernel = derece, kalınlaştırma derecesi
genisletilen_resim = cv2.dilate(kenari_testip_edilen_resim, (9,9))
cv2.imshow("genisletilen resim", genisletilen_resim)

# ERODE (ASINDIRMA) ( INCELTME)
# source, inceltme derecesi, miktar
inceltilen_resim = cv2.erode(genisletilen_resim, (7,7))
cv2.imshow("inceltilen resim", inceltilen_resim)

# resize işlemi
# ilk parametre resim, ikinci paramterse de (yeni boyut)
resize_edilen_resim = cv2.resize(atv_resmi, (500,500))
cv2.imshow("resize edilen resim", resize_edilen_resim)

# Crop işlemleri # resmin yüksekligi, genlisliği
#

kesilmis_resim = atv_resmi[1:200     , 1:400   ]
cv2.imshow('Cropped', kesilmis_resim)

# şekil cizdirme işlemleri

siyah_ekran=cv2.imread("/home/mef/Desktop/python_egitimi/blank.jpg")

# dikdörtgen
# rect , point 1 , point 2 , color (R,G,B) (100,0,255)
# dikdortgenin içi dolu olsun -1

#cv2.rectangle(siyah_ekran, (0,0), (100,100), ( 100,0 ,255), thickness = -1)
#cv2.imshow("dikdortgen cizilmis ekran",siyah_ekran)

# circle çember 

#cv2.circle(siyah_ekran, (100,100), 50, (255,0,0),thickness =-1)
#cv2.imshow("cember cizilmis ekran",siyah_ekran)

#cv2.line(siyah_ekran, (0,0), (200,200), (255,0,0),thickness = 10)
#cv2.imshow("line cizilmis ekran",siyah_ekran)


# 1. resim, text,
#cv2.putText(siyah_ekran, 'merhaba  hasan', (0,225), cv2.FONT_HERSHEY_COMPLEX, 1.0, (255,255,255), 4)
#cv2.imshow('Yazi yazdirilmis ekran', siyah_ekran)

kamera = cv2.VideoCapture(0) # kamera indisi 0, 1, 2

while True:

    acikmi, resim = kamera.read() # kameradan gelen görüntüleri aldık
    cv2.imshow("Gelen gercek zamanli goruntu",resim)

kamera.release() #  kamerayı sal göster 

# ezbere bilseniz de olur
cv2.waitKey(1)
cv2.destroyAllWindows()
