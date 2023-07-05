#!/usr/bin/env python
# coding: utf-8

# # Numpy Intro

# In[2]:


import numpy as np # numerical python, numpy kütüphanesi çağrılır ve np kısa yolu ile kullanılır.


# ![image.png](attachment:8d2b8262-4884-4f54-bed7-98fb33f0fed3.png)

# Python programlama dilinde çok boyutlu dizilerle uğraşmayı gerektiren hesaplamaları yapmak için geliştirilmiş modüldür. sadece vektör ve 2 boyutlu matrisleri değil, çok boyutlu matrisleri de destekler. burada destekten kasıt, bu veri yapılarını kolayca kullanmayı sağlayan indeksleme, nesne alanları ve yordamları barındırmasıdır. 
# 
# 1. Listeler elemanları tutarken içindeki her elemenın tek tek bilgisinide tutar(int, str vb.).
# 2. Arrayler tutmaz, tek bir bilgi tutar
# 3. Listelere göre daha performanslı bir şekilde bilgi tutar.
# 

# In[3]:


a = np.array([1,2,3,4,5]) # numpy array oluşturma
b = np.array([7,8,9,10,8]) # numpy array oluşturma
print(a)
print(b)


# In[4]:


a*b # matrisleri kolayca çarpabilirsiniz.


# In[5]:


a+b # matrisleri kolayca çıkartabilirsiniz


# # Numpy Array'i(Matris) oluşturma

# ![image.png](attachment:eb5aad91-bb5b-4268-9cfc-70b2a2adf0df.png)

# Matematikte matris veya dizey, dikdörtgen bir sayılar tablosu veya daha genel bir açıklamayla, toplanabilir veya çarpılabilir soyut miktarlar tablosudur. Dizeyler daha çok doğrusal denklemleri tanımlamak, doğrusal dönüşümlerde (lineer transformasyon) çarpanların takibi ve iki parametreye bağlı verilerin kaydedilmesi amacıyla kullanılırlar. Dizeylerin toplanabilir, çıkartılabilir, çarpılabilir, bölünebilir ve ayrıştırılabilir olmaları, doğrusal cebir ve dizey kuramının temel kavramı olmalarını sağlamıştır. 

# In[6]:


a = [8,9,10]
a = np.array(a) # bir listeyi array a dönüştürebilirsiniz.
print(a)

a = np.array([8,3,6]) # veya direk array oluşturabilirsiniz


# In[7]:


type(a) # tipine bakalım.


# In[8]:


c = np.array([3.14,5,6])
print(c)


# ![Screenshot_2020-06-22_10-02-02.png](attachment:0b57f415-0993-4735-813f-eebfcb69ace7.png)
# 
# Numpy bütün sayıları tek tipte saklar, ayrı ayrı tip bilgisi tutmaz.
# Listelerde ise her elemanın bilgisi tutulur.
# Numpy array lerinde tek çeşit veriler tutulur(int64, float64 vb.)
# Listelerde ise içiersinde bir çok çeşit tipe sahip veri saklar.
# Bu sayade numpy veri işleme makine öğrenmesi derin öğrenme gibi konularda daha performanslı oluyor.

# In[9]:


c = np.array([1,2,3,11,0], dtype="float32") # tanımlanırken içerdeki elemanların tipini belirleyebilirsiniz.
c


# In[10]:


c = np.zeros(10, dtype="int") # içersinde on adet sıfır elemanı bulunan bir array yarattık.
print(c)
# zeros methodu ile istediğimiz boyutta sıfırlardan oluşmuş bir matris yaratabiliriz.
d = np.zeros((10,10))

print("\n\n",d) # ona onluk float sıfırlandan oluşmuş matris.


# In[11]:


c = np.ones((3,5)) # üç satırlık beş sütünluk bir lerden oluşan matris.
print(c)
# ones methodu ile istediğimiz boyutta birlerden oluşmuş matris yaratabiliriz.
d = np.ones(10, dtype="int") # ona onluk int birlerden oluşmuş matris.


# In[12]:


c = np.full((5,8), 58, dtype="float64") # 5 e 8 lik 58 lerden oluşan float64 tip biçimine sahip matris.
# full methodu ile istediğimiz boyutta istediğimiz sayılardan oluşan bir matris yaratabiliriz.
c


# In[13]:


d = np.arange(0,100,5) # 0 dan 100 e kadar 5 er 5 er atlayarak tek boyutlu bir matris oluşturduk.
# arange methodu istediğimiz değerler arasında istediğimiz katsayılarla bir matris oluşturabiliriz.
d


# In[14]:


a = np.linspace(0,5,10) # sıfır ile beş arasında 10 tane rastgele değer oluşturdu.
# bu method ile istediğimiz değerler arasında istediğimiz kadar rastgele sayılardan oluşan bir matris oluşturabiliriz.
a


# In[15]:


e = np.random.normal(12,8,(3,6)) # ortalaması on, standart sapması dört, üç satır altı sütündan oluşan bir matris.
# bu method ile rastgele sayılardan ve istediğimiz boyuta sahip bir matris tanımladık, doğılımını biz belirledik(ortalama, standart sapması)
e


# In[16]:


z = np.random.randint(0,200, (5,5)) # 0 la 200 arasında 5 e 5 lik rastgele int değerlerden oluşmuş bir matris.
# bu method ile istediğimiz değerler arasında istediğimiz boyuta sahip int bir matris oluşturabiliriz.
z


# # Numpr Array 'leri Özellikleri
# 
# * ndim : boyut sayısı
# * shape : boyut bilgisi
# * size : toplam eleman sayısı
# * dtype : array veri tipi

# In[17]:


a = np.random.randint(10, size = 10) # sıfırdan 10 a kadar on elemanlı bir matris oluşturduk
a


# In[18]:


a.ndim # bir boyutlu 
# bize boyut bilgisini verir


# In[19]:


a.shape # 10 elemanlı tek boyutlu matris
# matrisin boyut bilgisi hakkında bilgi verir.


# In[20]:


a.size # on elemanı var
# matrisin eleman sayısını geri döndürür.


# In[21]:


a.dtype # int64 tipe sahip matris
# matrisin tipini geri döndürür.


# In[22]:


a = [[0,5,2],[2,3,6]] # 2 satir, 2 sütünluk bir matris.
b = np.array(a)
b


# In[23]:


b.ndim # iki boyutlu 
# bize boyut bilgisini verir


# In[24]:


b.shape # iki satir, iki sutunu olan bir matris.
# matrisin boyut bilgisi hakkında bilgi verir.


# In[25]:


b.size # 3*2 den 6 elemanı var
# matrisin eleman sayısını geri döndürür.


# In[26]:


b.dtype # int64 tipe sahip matris
# matrisin tipini geri döndürür.


# # Yeniden Şekillendirme : Reshaping

# In[27]:


a = np.arange(1,10)
print("Düzenlenmeden hali : \n\n",a)
# reshape metodu sayesinde matrislerin satir ve sütünlarında önemli değişiklikler yaparak boyutunu değistitiriz.
a = a.reshape(3,3)
print("Düzenleden sonraki hali : \n\n",a)


# In[28]:


a = np.random.randint(0,100,(10))
print(a)

eleman = a.shape[0]

print(eleman) # on elemanlı

# eğer bu matrisi tekrar düzenlemek istiyorsak:
# satir*sütün == eleman
# aksi halde hata verir, ya yeterli eleman yoktur, yada fazladan eleman kalır.
# örn:

a = a.reshape(5,2)
print(a)

if a.shape[0]*a.shape[1] == eleman:
    
    print("Hata yoktur, düzenleme basarılı")
    
# örn:

try:
    
    a.reshape(3,3) # 9 eleman gerekli
    
except:
    
    print("Hata var. yetiri kadar eleman bulamıyorum")


# In[29]:


a = np.arange(1,10).reshape(3,3) # başka bir düzenleme işlemi
a


# In[30]:


a = np.arange(0,10)
print(a)
print(a.ndim) # tek boyutlu matris

a = a.reshape((1,10))
print(a)
print(a.ndim) # artık matristir, bir satir 10 sütundan oluşur. vektör barındırır.


# # Array Birleştirme (Concatenation)

# In[31]:


a = np.array([0,1,2,3])

b = np.array([3,4,5,6,7,8,9])

print(np.concatenate([a,b])) # iki array birleştirip tek bir array haline getirir.

# üç tane dört tane vs.. adet array birleştirilebilir
c = np.array([0,1,2,3,99,81,2])
print(np.concatenate([a,b,c]))


# In[32]:


a = np.array([[5,6,3],[1,2,3]])
print(np.concatenate([a,a])) # satır bazında birleştirme yapar.


# In[33]:


a = np.array([[5,6,3],[1,2,3]])
print(np.concatenate([a,a], axis=1)) # sütün bazında birleştirme işlemi yapar 
# axis eksen belirtmek için kullanılır. 0 satirlari, 1 sütünları temsil eder


# # Array Ayırma : Dilimleme

# In[34]:


# 1. yöntem

a = np.array([1,2,3,88,89,90,3,2,1])
# 3 er 3 er bölme işlmi yaptık, Python listeleri nasıl dilimliyorsayl numpy arrayleri de aynı şekilde dilimleyebiliriz.
print(a[0:3])
print(a[3:6])
print(a[6:9])


# In[35]:


# 2. yöntem

a = np.split(a, [3,6]) # split listelerde bölme işlemiyapar
# array larda kullanımı ise, a arrayını 3'e kadar ve 6' ya kadar parçalamasını istedik.
#n indeksi verirseniz n+1 adet array geri döndürür.
print(a[0],a[1],a[2])


# In[36]:


# iki boyutlu array parçalama

a = np.arange(20)
a = a.reshape(4,5)
print(a)


# In[37]:


np.vsplit(a, [2]) # 2 ye kadar satira göre parçalama yaptık. Yatay olarak.


# In[38]:


np.hsplit(a, [3]) # sütünları parçaladı, dikey olarak.


# In[39]:


# Her parçalama işleminden sonra geriye bir liste döndürür. arraylar bu listenin içindedir.


# In[40]:


a = np.arange(100)

a = a.reshape(10,10)
print(a)


# In[41]:


print(a[:,8]) # sütün 8 den satırların hepsini aldı


# In[42]:


print(a[7,:]) # 7. satır sütünların tamamı


# In[43]:


print(a[3:6,:]) # 3 ve 6. satırlar ve aralarındaki satırları ve sütünların tamamı.


# In[44]:


print(a[:,1:8]) # sütünların 1 ve 8 dahil alan ve satirların tamamı.


# # Array Sıralama : Sorting

# In[45]:


# tek boyutlu

a = np.array([0,9,8,5,6,3,2,4]) # bunu belli bir kurala göre sıralamalıyız.
print(np.sort(a)) # arrayı küçükten büyüyye doğru sıralar.

# birde kendi algoritmamızı çalıştıralım

print(a)


for i in range(0,a.shape[0]):


    for j in range(0,a.shape[0]):

        if a[i] < a[j]:

            gecici = a[i]

            a[i] = a[j]

            a[j] = gecici


print(a)


# In[46]:


# 2 boyutlu array
a = np.random.randint(0,100, (5,5))
a


# In[47]:


np.sort(a, axis=1) # satirlarda sıralma işlemi yapar.


# In[48]:


np.sort(a, axis=0) # sütünlarda sıralama işlemi yapar.


# ## index ile elemanlara erişmek

# In[49]:


a = np.random.randint(0,100, (5,5))
print(a)
print(a[0,4]) # a nın 0. satirindan 4. sütünundaki elemanı alır


# In[50]:


print(a[4,2]) # 4. satirdan 2 sütündaki elemanı alır.


# In[51]:


print(a[2]) # 2. satiri alir


# In[52]:


print(a[:,3]) # 3. sutun


# In[53]:


print(a[-1]) # en sondaki satir


# In[54]:


print(a[:,-1]) # en sondaki sutun


# In[55]:


print(a[0:2,2:4]) # 0 ve 2. satir ve 2 ve 4. sütün


# In[56]:


a = np.random.randint(15, size=(5))
print(a)
print(a[0]) # a arrayin 0. elemanı
print(a[4]) # a arrayinin 4. elemanı


# In[57]:


a[0::2] # ikişer ikişer atlayarak yazdırır.


# In[58]:


a[1:4:3] # 1. indexten 4. indexe kadar 3 er 3 er yazdırır.


# In[59]:


m = np.random.randint(10, size=(5,5))

print(m)


# In[60]:


print(m[0][2]) # 0. satır, 2. sütündaki eleman
print(m[0,2]) # 0. satır, 2. sütündaki eleman


# In[61]:


m[-1:,:] # son satır.


# #### Önemli **

# In[62]:


m = np.random.randint(10, size = (10,10))
print(m)


# In[63]:


alt_küme = m[0:3,0:6]
print(alt_küme)


# In[64]:


alt_küme[0][0] = -99
print(alt_küme)
print(m)
# gördüğünüz gibi alt kümede yaptığımız işlem ana arraya da yansıdı, sebebi bellekte iki dizide aynı bölgeyi işaret ediyor.


# In[65]:


a = np.random.randint(10, size = (5,5))
c = a
print(a,"\n\n",c,"\n")

a[0][0] = -188

print("Değisiklikten sonra\n\n",a,"\n\n",c)
# aynı şekilde a arrayinde yaptığımız işlem c arraya da yansıdı, sebebi bellekte iki dizide aynı bölgeyi işaret ediyor.


# In[66]:


a = np.random.randint(10, size = (5,5))

# bu iki yöntem ile bellekte yeni bir alan yaratıp array ları bu bölgelere taşırız.
c = np.array(a[:,:])
z = a.copy()

a[0,0] = -2
print(a,"\n\n",z)


# ## Fancy index

# In[67]:


m = np.random.randint(10, size = (10))
print(m)
print("\n")
getir = [1,5,3] # listedeki indexleri getirir.
print(m[getir])


# In[68]:


m = np.random.randint(10, size = (10,10))

print(m)
print("\n")
satir = [0,3]
sutun = [0,6]
# 0. satir 0 . sütün elemanı
# 3. satir 6. sütün elemanı
print(m[satir,sutun])


# In[69]:


# basit index ile fancy index

print(m[0, [1,2,3]]) # 0. satir ilk üç sütün


# In[70]:


# slays ve fancy index

print(m[0:2, [1,2,3]]) # 0 dan 2. satıra kadar ve ilk üç sütünu yazdırır.


# ## koşullu işlemler

# In[71]:


v = np.random.randint(10, size = (10,10))

# elemanı 8 den büyük olan değerlerin indexinde true değer döndürür.
# aksi halde false
print(v>8)
print("\n")

print(v[v>8]) # arrayın 8 den büyük değerlerini yazdırır.


# In[72]:


# elemanı 3 den küçük ve eiit olan değerlerin indexinde true değer döndürür.
# aksi halde false
print(v<=3)

# arrayın 3 den küçük ve eşit değerlerini yazdırır.
print("\n\n",v[v<=3])


# In[73]:


print(v==8) # 8 e eşit olan değerler

# 8 e eşit olan değerlerin yazılması
print("\n\n",v[v==8])


# In[74]:


print(v!=8) # 8 e eşit olmayan değerler

# 8 e eşit olmayan değerlerin yazılması
print("\n\n",v[v!=8])


# ## Matematiksel işlemler

# In[75]:


print(v*2) # arrayın iki katı

print("\n")
print(v*v) # arayın karesi

print("\n")
print(v/5) # arayın elemanlarının beş e bölümü

print("\n")
print(v-8) # arayın elemanlarından sekiz çıkartmak

print("\n")
print(v+8) # arayın elemanlarına sekiz eklemek

print("\n")
print(v%2) # arayın iki ile modu


# In[76]:


np.subtract(v,5) # aray dan 5 çıkartır


# In[77]:


np.add(v,9) # aray a 9 ekler


# ![20200718_095720.jpg](attachment:3b1891ea-10b6-45c3-8581-f7abdf98297d.jpg)

# In[78]:


np.multiply(v,8) # elemanlarını 8 ile çarpar


# In[79]:


np.divide(v,3) # elemanları 3 e böler


# In[80]:


np.power(v,3) # matrisin küpü


# In[81]:


np.mod(v,2) # 2 ile modu


# In[82]:


np.absolute(v) # matrisin mutlak değeri


# In[83]:


np.sin(360) # sin 360


# In[84]:


np.cos(180) # cos 180


# In[85]:


np.log10(v) # tüm elemanları log2 tabanına alır


# In[86]:


get_ipython().run_line_magic('pinfo', 'np')
# numpy ın ana dökümantasyonu
# genel bilgiler ve alt paketler


# ![Screenshot_2020-07-17 Cheat sheet Numpy Python copy indd - Numpy_Python_Cheat_Sheet pdf.png](attachment:ba2c61ef-d469-4d4e-97c8-21a4c2e97d9f.png)

# # Numpy ile iki bilinmeyenli denklem çözümü

# * 5 * X + Y = 12
# 
# * X + 3 * Y = 10
# 
# X ve Y bilinmeyenleri bulalım.

# In[87]:


a = np.array([[5,1], [1,3]])
b = np.array([12, 10])

z = np.linalg.solve(a, b)
print("X = ",z[0],", Y = ",z[1])


# In[ ]:




