# 1. Giriş – Deep Learning ve CNN Neden Var?

## Giriş
Önceki derslerde, tablo verileri ve sayısal değerler üzerinde Machine Learning algoritmaları ile modeller kurduk.  
Ancak iş görsellere geldiğinde, klasik ML yöntemleri bazı ciddi sınırlamalara sahip.

---

## Klasik ML ile Görsel İşleme Zorlukları
- **Manuel özellik çıkarımı zorunluluğu**  
  Görsellerden kenar, renk, köşe, doku gibi özellikler önceden belirlenip çıkarılmalıdır.  
  Örneğin HOG, SIFT, SURF gibi yöntemler bu amaçla kullanılır.
- **Yüksek boyutluluk**  
  256x256 piksel boyutunda bir görsel, 65.536 özellik içerir. Bu boyut hem hesaplama yükünü artırır hem de overfitting riskini yükseltir.
- **Konum ve ölçek hassasiyeti**  
  Objenin konumu veya boyutu değiştiğinde modelin doğru tahmin yapması zorlaşır.

---

## Deep Learning'in Avantajları
- **Otomatik özellik çıkarımı**  
  CNN’ler, görsellerdeki ayırt edici özellikleri kendisi öğrenir, manuel olarak çıkarılmasına gerek kalmaz.
- **Katmanlı öğrenme**  
  İlk katmanlar kenar ve basit şekilleri, orta katmanlar daha karmaşık yapıları, üst katmanlar ise nesnenin bütününü tanır.
- **Konuma duyarsızlık**  
  Obje biraz sağa veya sola kaymış olsa bile tanınabilir.
- **Daha az mühendislik ihtiyacı**  
  Feature engineering yerine veri doğrudan modele verilir.

---

## CNN ile ML Arasındaki Temel Fark
- **ML yaklaşımı:** Önce nesnenin tüm özellikleri tanımlanır, model bu özelliklerle eğitilir.  
- **CNN yaklaşımı:** Modele çok sayıda örnek gösterilir, model ayırt edici özellikleri kendisi bulur.

---

## Bu Derste İşlenecek Konular
1. CNN'in temel yapısının anlaşılması  
2. Sıfırdan bir CNN ile basit image classification projesi (MNIST)  
3. Transfer learning ile hazır bir modelin kendi verimize uyarlanması

# 2. CNN Temelleri

## CNN Nedir?
Convolutional Neural Network (CNN), özellikle görsel veriler üzerinde yüksek başarı gösteren bir yapay sinir ağı mimarisidir.  
Görsellerdeki uzamsal (spatial) ve yerel (local) ilişkileri öğrenebilme yeteneği sayesinde, klasik yapay sinir ağlarına göre daha verimli çalışır.

---

## Temel Katmanlar

### 1. Convolution Katmanı
- Görev: Giriş verisi üzerinde filtreler (kernel) kullanarak özellik haritaları (feature map) çıkarır.
- Her filtre, belirli bir özelliği (kenar, köşe, doku vb.) algılar.
- Stride, padding gibi hiperparametreler ile çıktı boyutu kontrol edilir.

### 2. Aktivasyon Fonksiyonu (ReLU)
- Görev: Doğrusal olmayan özellikler ekler.
- Negatif değerleri sıfırlar, pozitifleri olduğu gibi geçirir.

### 3. Pooling Katmanı
- Görev: Özellik haritalarının boyutunu küçültür.
- En yaygın yöntem: **Max Pooling** (her bölgedeki en büyük değeri alır).
- Avantaj: Hesaplama maliyetini azaltır, overfitting riskini düşürür.

### 4. Flatten Katmanı
- Görev: 2B özellik haritalarını 1B vektöre dönüştürür.
- Bu vektör, tam bağlı (dense) katmanlara giriş olarak verilir.

### 5. Dense (Tam Bağlı) Katman
- Görev: Öğrenilen özelliklere göre sınıflandırma yapar.
- Son katman genellikle **softmax** (çok sınıflı) veya **sigmoid** (ikili sınıf) aktivasyonu kullanır.

---

## CNN Akış Örneği
1. **Girdi:** 28x28 piksel gri tonlamalı görsel  
2. **Conv Katmanı:** 32 adet 3x3 filtre ile kenar/doku bilgisi çıkarılır  
3. **ReLU:** Negatif değerler sıfırlanır  
4. **Max Pooling:** 2x2 pencereler ile boyut yarıya indirilir  
5. **Conv Katmanı:** Daha karmaşık özellikler öğrenilir  
6. **Flatten:** 2B → 1B dönüşümü  
7. **Dense Katman:** Tam bağlı katman ile sınıflandırma

---

## CNN’in Avantajlı Olma Sebepleri
- Parametre paylaşımı (aynı filtrenin tüm görüntü üzerinde kullanılması)
- Yerel bağlantılar (her nöron yalnızca küçük bir bölgeden veri alır)
- Boyut küçültme ile hesaplama verimliliği


# 3. Proje 1 – CNN ile MNIST

## Proje Amacı
Bu projede, CNN mimarisi kullanarak **MNIST el yazısı rakam veritabanı** üzerinde sınıflandırma modeli geliştireceğiz.  
MNIST, 28x28 boyutunda gri tonlamalı 70.000 el yazısı rakam görüntüsünden oluşur (0–9 arası).

---

## Adımlar

### 1. Kütüphanelerin Yüklenmesi
```python
import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

# MNIST veri setini yükle
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Giriş verisini normalize et (0-255 → 0-1)
x_train = x_train[..., tf.newaxis] / 255.0
x_test = x_test[..., tf.newaxis] / 255.0

model = models.Sequential([
    layers.Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
    layers.MaxPooling2D((2,2)),
    layers.Conv2D(64, (3,3), activation='relu'),
    layers.MaxPooling2D((2,2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

history = model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))

plt.plot(history.history['accuracy'], label='Eğitim Doğruluğu')
plt.plot(history.history['val_accuracy'], label='Doğrulama Doğruluğu')
plt.xlabel('Epoch')
plt.ylabel('Doğruluk')
plt.legend()
plt.show()

# 4. Proje 2 – Transfer Learning (MobileNetV2)

## Proje Amacı
Bu projede, **MobileNetV2** gibi önceden eğitilmiş bir CNN modelini (ImageNet veri seti ile eğitilmiş) kullanarak  
**CIFAR-10 veri setindeki kedi ve köpek görsellerini** sınıflandıracağız.  
Amaç, daha az veri ve daha kısa eğitim süresi ile yüksek doğruluk elde etmek.

---

## Adımlar

### 1. Kütüphanelerin Yüklenmesi
```python
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import matplotlib.pyplot as plt

# CIFAR-10 veri setini yükle
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()

# Kedi = 3, Köpek = 5 etiketleri
classes = [3, 5]

train_mask = (y_train.flatten() == 3) | (y_train.flatten() == 5)
test_mask = (y_test.flatten() == 3) | (y_test.flatten() == 5)

x_train, y_train = x_train[train_mask], y_train[train_mask]
x_test, y_test = x_test[test_mask], y_test[test_mask]

# MobileNetV2 giriş ön işleme
x_train = preprocess_input(x_train)
x_test = preprocess_input(x_test)

# Etiketleri ikili sınıfa dönüştür (kedi=0, köpek=1)
y_train = (y_train == 5).astype(int)
y_test = (y_test == 5).astype(int)

# Önceden eğitilmiş MobileNetV2 taban modeli
base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(32,32,3))
base_model.trainable = False  # Ağırlıklar donduruldu

# Üst katmanlar
model = models.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

history = model.fit(x_train, y_train, epochs=3, validation_data=(x_test, y_test))

plt.plot(history.history['accuracy'], label='Eğitim Doğruluğu')
plt.plot(history.history['val_accuracy'], label='Doğrulama Doğruluğu')
plt.xlabel('Epoch')
plt.ylabel('Doğruluk')
plt.legend()
plt.show()
```
# Beklenen Sonuç
- Daha kısa eğitim süresi (3 epoch içinde yüksek doğruluk)
- Transfer learning ile az veriyle bile iyi sonuç alınması
- Taban modelin dondurulması sayesinde overfitting riskinin azalması

# 5. Tartışma ve Kapanış

Bu ders boyunca iki farklı yaklaşımı gördük:

## CNN ile Sıfırdan Model Eğitimi
- Avantajlar:
  - Model mimarisi tamamen ihtiyaçlara göre tasarlanabilir.
  - Küçük veri setlerinde hızlı deneyler yapılabilir.
- Dezavantajlar:
  - Yüksek doğruluk için çok sayıda veri gerekir.
  - Eğitim süresi uzun olabilir.

## Transfer Learning ile Model Eğitimi
- Avantajlar:
  - Daha az veri ile yüksek doğruluk.
  - Eğitim süresi çok daha kısa.
  - Önceden öğrenilmiş özelliklerden yararlanılır.
- Dezavantajlar:
  - Hazır model mimarisi sınırlıdır.
  - Bazı durumlarda fine-tuning gerekebilir.

**Genel Sonuç:**  
Gerçek dünya projelerinde, veri seti küçükse transfer learning genellikle en iyi seçenektir.  
Büyük ve kapsamlı veri setleri olduğunda ise sıfırdan CNN eğitimi mantıklı olabilir.

---

# 6. Ödev

1. **Veri Seti Değiştirme**  
   - MNIST yerine Fashion-MNIST veri seti ile aynı CNN mimarisini deneyin.
   
2. **Düzenlileştirme (Regularization)**  
   - Modelinize `Dropout` katmanları ekleyin.  
   - Farklı dropout oranlarını deneyerek doğruluk farkını gözlemleyin.

3. **Kendi Veri Setinizi Kullanma**  
   - İnternetten iki sınıflı küçük bir veri seti oluşturun (örneğin: araba vs bisiklet).  
   - MobileNetV2 veya başka bir hazır model ile eğitin.

4. **Veri Çoğaltma (Data Augmentation)**  
   - `ImageDataGenerator` veya `tf.keras.layers.RandomFlip/RandomRotation` gibi yöntemlerle eğitim verinizi çeşitlendirin.  
   - Augmentation öncesi ve sonrası doğruluk sonuçlarını karşılaştırın.

5. **Fine-Tuning Denemesi**  
   - Transfer learning projesinde, taban modelin son birkaç katmanını açarak yeniden eğitin.  
   - Performans farkını raporlayın.
