
# VERİ YAPILARI ÖDEVİ
# Arama ve Sıralama Algoritmaları
# Hazırlayan: İbrahim Türköz

# LINEAR SEARCH (Doğrusal Arama)

def linear_search(liste, hedef):
    # Eleman sayısını almak için değişken
    uzunluk = len(liste)
    # Listenin başından sonuna kadar dön
    for i in range(uzunluk):
        # Eğer o anki eleman hedefe eşitse
        if liste[i] == hedef:
            # Elemanın indeksini döndür
            return i
    # Eğer eleman bulunamazsa -1 döndür
    return -1

# BINARY SEARCH (İkili Arama)
# NOT: Liste sıralı olmalıdır!

def binary_search(liste, hedef):
    # Aramanın başlayacağı sol indeks
    sol = 0
    # Aramanın biteceği sağ indeks
    sag = len(liste) - 1
    # Sol indeks sağdan küçük veya eşit olduğu sürece devam et
    while sol <= sag:
        # Orta noktayı hesapla
        orta = (sol + sag) // 2
        # Eğer orta eleman hedefe eşitse
        if liste[orta] == hedef:
            # İndeksi döndür
            return orta
        # Eğer hedef orta elemandan büyükse
        elif liste[orta] < hedef:
            # Sol sınırı ortaya göre güncelle
            sol = orta + 1
        # Eğer hedef orta elemandan küçükse
        else:
            # Sağ sınırı ortaya göre güncelle
            sag = orta - 1
    # Eleman bulunamazsa -1 döndür
    return -1

# BUBBLE SORT

def bubble_sort(liste):
    # Listenin uzunluğunu al
    n = len(liste)
    # Liste üzerinde n kez dön
    for i in range(n):
        # Her turda en büyük eleman sona gider
        for j in range(0, n - i - 1):
            # Eğer soldaki eleman sağdakinden büyükse
            if liste[j] > liste[j + 1]:
                # Yer değiştir (swap)
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
    # Sıralanmış listeyi döndür
    return liste

# SELECTION SORT

def selection_sort(liste):
    # Listenin uzunluğunu al
    n = len(liste)
    # Listenin tamamında dön
    for i in range(n):
        # En küçük elemanın indeksini başlangıçta i kabul et
        min_index = i
        # i’den sonraki elemanlarda dön
        for j in range(i + 1, n):
            # Eğer daha küçük bir eleman bulunursa
            if liste[j] < liste[min_index]:
                # Yeni minimum indeksini güncelle
                min_index = j
        # Bulunan en küçük elemanı başa al
        liste[i], liste[min_index] = liste[min_index], liste[i]
    # Sıralanmış listeyi döndür
    return liste

# INSERTION SORT

def insertion_sort(liste):
    # Listenin 2. elemanından başlayarak dön
    for i in range(1, len(liste)):
        # O anki elemanı geçici değişkene al
        anahtar = liste[i]
        # Önceki indeksi al
        j = i - 1
        # Anahtar elemandan büyük olanları sağa kaydır
        while j >= 0 and anahtar < liste[j]:
            # Elemanı sağa kaydır
            liste[j + 1] = liste[j]
            # Bir önceki elemana geç
            j -= 1
        # Anahtar elemanı doğru konuma yerleştir
        liste[j + 1] = anahtar
    # Sıralanmış listeyi döndür
    return liste

# MERGE SORT

def merge_sort(liste):
    # Eğer liste 1 veya daha az elemanlıysa
    if len(liste) <= 1:
        # Liste zaten sıralıdır
        return liste
    # Listenin orta noktasını bul
    orta = len(liste) // 2
    # Listenin sol yarısını al
    sol = liste[:orta]
    # Listenin sağ yarısını al
    sag = liste[orta:]
    # Sol tarafı recursive olarak sırala
    sol = merge_sort(sol)
    # Sağ tarafı recursive olarak sırala
    sag = merge_sort(sag)
    # İki sıralı listeyi birleştir
    return merge(sol, sag)

def merge(sol, sag):
    # Birleştirilmiş listeyi tutacak boş liste
    sonuc = []
    # Sol ve sağ listeler için indeksler
    i = 0
    j = 0
    # Her iki liste bitene kadar devam et
    while i < len(sol) and j < len(sag):
        # Küçük olanı seç
        if sol[i] < sag[j]:
            sonuc.append(sol[i])
            i += 1
        else:
            sonuc.append(sag[j])
            j += 1
    # Kalan elemanları ekle
    sonuc.extend(sol[i:])
    sonuc.extend(sag[j:])
    # Birleştirilmiş listeyi döndür
    return sonuc

# QUICK SORT

def quick_sort(liste):
    # Eğer liste 1 veya daha az elemanlıysa
    if len(liste) <= 1:
        # Listeyi olduğu gibi döndür
        return liste
    # Pivot olarak ortadaki elemanı seç
    pivot = liste[len(liste) // 2]
    # Pivot’tan küçük elemanları al
    kucukler = [x for x in liste if x < pivot]
    # Pivot’a eşit elemanları al
    esittir = [x for x in liste if x == pivot]
    # Pivot’tan büyük elemanları al
    buyukler = [x for x in liste if x > pivot]
    # Recursive olarak sırala ve birleştir
    return quick_sort(kucukler) + esittir + quick_sort(buyukler)

# TEST

if __name__ == "__main__":
    # Örnek liste oluştur
    veri = [65, 9, 28, 49, 8, 92]
    # Linear Search testi
    print("Linear Search sonucu:", linear_search(veri, 23))
    # Önce sıralama yap binary search için
    sirali_veri = merge_sort(veri)
    # Binary Search testi
    print("Binary Search sonucu:", binary_search(sirali_veri, 23))
    # Diğer sıralamaların çıktıları
    print("Bubble Sort:", bubble_sort(veri.copy()))
    print("Selection Sort:", selection_sort(veri.copy()))
    print("Insertion Sort:", insertion_sort(veri.copy()))
    print("Merge Sort:", merge_sort(veri.copy()))
    print("Quick Sort:", quick_sort(veri.copy()))
