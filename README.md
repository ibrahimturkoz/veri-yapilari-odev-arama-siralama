#  Veri Yapıları Ödevi – Arama ve Sıralama Algoritmaları

##  **Proje Hakkında**
Bu proje, Veri Yapıları dersi kapsamında arama ve sıralama algoritmalarının hem teorik hem de pratik olarak anlaşılması amacıyla hazırlanmıştır.

**Amaç yalnızca algoritmaları çalıştırmak değil;**
* Mantığını kavramak
* Zaman karmaşıklıklarını analiz etmek
* Birbirleriyle karşılaştırmak
* Gerçek hayatta hangi durumda hangisinin tercih edilmesi gerektiğini anlamaktır.

Projede 2 arama ve 5 sıralama algoritması **Python** dili kullanılarak sıfırdan kodlanmıştır.

---

##  ** Arama Algoritmaları**

### **1.1 Linear Search (Doğrusal Arama)**
** Çalışma Mantığı**
* Listenin başından sonuna kadar tek tek kontrol eder.
* Hedef değeri bulduğu anda işlemi durdurur.
* Liste sıralı olmak zorunda değildir.
* Basit ama büyük veri için yavaştır.

** Zaman Karmaşıklığı**
| Durum | Karmaşıklık |
| :--- | :--- |
| **En iyi durum** | $O(1)$ |
| **Ortalama** | $O(n)$ |
| **En kötü durum** | $O(n)$ |

> En kötü durumda tüm elemanlar kontrol edilir.

### **1.2 Binary Search (İkili Arama)**
** Çalışma Mantığı**
* Sadece sıralı listelerde çalışır.
* Listenin ortasını kontrol eder.
* Hedef küçükse sol yarıya, büyükse sağ yarıya geçer.
* Her adımda veri kümesini ikiye böler.
* Bu nedenle çok daha hızlıdır.

** Zaman Karmaşıklığı**
| Durum | Karmaşıklık |
| :--- | :--- |
| **En iyi durum** | $O(1)$ |
| **Ortalama** | $O(\log n)$ |
| **En kötü durum** | $O(\log n)$ |

> Büyük veri kümelerinde Linear Search’e göre çok daha verimlidir.

---

##  ** Sıralama Algoritmaları**
Projede aşağıdaki sıralama algoritmaları uygulanmıştır:
* Bubble Sort
* Selection Sort
* Insertion Sort
* Merge Sort
* Quick Sort

### **2.1 Bubble Sort**
** Mantık**
* Komşu elemanları karşılaştırır ve büyük olanı sona doğru taşır.
* Her turda en büyük eleman listenin sonuna yerleşir.

** Karmaşıklık**
* **Ortalama:** $O(n^2)$
* **En kötü:** $O(n^2)$
* **En iyi (iyileştirilmiş versiyonda):** $O(n)$
* *Yavaş ama öğretici bir algoritmadır.*

### **2.2 Selection Sort**
** Mantık**
* Her turda en küçük elemanı bulur ve başa yerleştirir.

** Karmaşıklık**
* **Tüm durumlar:** $O(n^2)$
* *Karşılaştırma sayısı sabittir, ancak swap sayısı azdır.*

### **2.3 Insertion Sort**
** Mantık**
* Kart dizme mantığı ile çalışır.
* Elemanları tek tek doğru pozisyona yerleştirir.

** Karmaşıklık**
* **En iyi:** $O(n)$ (liste zaten sıralıysa)
* **Ortalama:** $O(n^2)$
* **En kötü:** $O(n^2)$
* *Küçük ve kısmen sıralı listelerde oldukça verimlidir.*

### **2.4 Merge Sort**
** Mantık**
* "Böl ve Fethet" (Divide and Conquer) yaklaşımı kullanır.
* Listeyi ikiye böler.
* Alt listeleri sıralar.
* Sonra birleştirir.

** Karmaşıklık**
* **En iyi:** $O(n \log n)$
* **Ortalama:** $O(n \log n)$
* **En kötü:** $O(n \log n)$
* *Ek bellek kullanır fakat performansı stabildir.*

### **2.5 Quick Sort**
** Mantık**
* Bir pivot seçer.
* Küçükleri sola, büyükleri sağa koyar.
* Alt listeleri recursive olarak sıralar.

** Karmaşıklık**
| Durum | Karmaşıklık |
| :--- | :--- |
| **En iyi** | $O(n \log n)$ |
| **Ortalama** | $O(n \log n)$ |
| **En kötü** | $O(n^2)$ |

> Pratikte genellikle en hızlı sıralama algoritmalarından biridir.

---

##  **Algoritmaların Karşılaştırılması**

| Algoritma | En İyi Durum | Ortalama Durum | En Kötü Durum | Bellek Kullanımı |
| :--- | :---: | :---: | :---: | :---: |
| **Linear Search** | $O(1)$ | $O(n)$ | $O(n)$ | $O(1)$ |
| **Binary Search** | $O(1)$ | $O(\log n)$ | $O(\log n)$ | $O(1)$ |
| **Bubble Sort** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ |
| **Selection Sort** | $O(n^2)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ |
| **Insertion Sort** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ |
| **Merge Sort** | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ |
| **Quick Sort** | $O(n \log n)$ | $O(n \log n)$ | $O(n^2)$ | $O(\log n)$ |

---

##  **Kod Nasıl Çalıştırılır?**

### ** Python yüklü olmalıdır**
Bilgisayarda Python 3 kurulu olmalıdır.
Kontrol etmek için: `python --version` veya `python3 --version`

### ** Dosyayı Çalıştırma**
Terminal veya komut satırında proje klasörüne girip:
`python arama_siralama.py` veya `python3 arama_siralama.py`
komutunu çalıştırmanız yeterlidir.
> Program test verisi üzerinde tüm algoritmaları çalıştıracaktır.

---

##  **Sonuç ve Değerlendirme**
Bu proje sayesinde:
* Arama algoritmalarının mantığı kavranmıştır.
* Sıralama algoritmaları karşılaştırılmıştır.
* Zaman karmaşıklıkları analiz edilmiştir.
* Recursive ve iterative yaklaşımlar uygulanmıştır.
* Böl ve Fethet stratejisi pratiğe dökülmüştür.
* Teorik bilgi ile pratik uygulama birleştirilmiştir.

---

##  **Hazırlayan**

**İbrahim Türköz**

**25019921056**

**Veri Yapıları Dersi**

**Arama ve Sıralama Algoritmaları Ödevi**
