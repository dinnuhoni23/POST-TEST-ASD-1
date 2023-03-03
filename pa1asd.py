import os
os.system ('cls')
import random

def mergeSort(data):
    if len(data) > 1:

# mid adalah titik dimana array dibagi menjadi dua subarray
        mid = len(data) // 2
        left_data = data[:mid]
        right_data = data[mid:]

# Mengurutkan dua bagian
        mergeSort(left_data)
        mergeSort(right_data)

        i=j=k= 0

# Hingga kita mencapai salah satu ujung left_data atau right_data, pilih yang
#lebih besar di antara elemen left_data dan right_data letakkan di posisi yang benar
        while i < len(left_data) and j < len(right_data):
            if left_data[i] < right_data[j]:
                data[k] = left_data[i]
                i += 1
            else :
                data[k] = right_data[j]
                j += 1
            k += 1

# Saat kita kehabisan elemen di left_data atau right_data, ambil elemen yang tersisa dan masukkan
        while i < len(left_data):
            data[k] = left_data[i]
            i += 1
            k += 1
 
        while j < len(right_data):
            data[k] = right_data[j]
            j += 1
            k += 1

data =  [random.randint(10,100) for i in range(10)]
print(f"|| Merge sort belum urut : ", data)
mergeSort(data)
print(f"|| Merge sort terurut : ", data)

################################################################################################################################################
# Berfungsi untuk mempartisi array berdasarkan elemen pivot def partition (array, rendah, tinggi):
def partition(array, low, high):

# Memilih elemen pivot
    pivot = array[high]
    i = low - 1

# Meletakkan elemen yang lebih kecil dari pivot di sebelah kiri dan lebih besar dari pivot di sebelah kanan pivot
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

def quickSort(array, low, high):
    if low < high:

# Memilih posisi pivot dan letakkan semua elemen lebih kecil dari pivot di kiri dan lebih besar dari pivot di kanan
        pi = partition(array, low, high)

# Mengurutkan elemen di sebelah kiri pivot
        quickSort(array, low, pi - 1)

# Mengurutkan elemen di sebelah kanan pivot
        quickSort(array, pi + 1, high)

data =  [random.randint(20,100) for i in range(10)]
print (90*"=")
print(f"|| Quicksort belum urut : ", data)
size = len(data)
quickSort(data, 0, size - 1)
print(f"|| Quicksort terurut : ", data)

################################################################################################################################################
def shell(list):
    n = len (list)

# Mengatur ulang elemen pada setiap interval n/2
    gap = n // 2

    while gap > 0:
        for i in range (gap, n):
            temp = list[i]
            j=i
            while j >= gap and list [j-gap] > temp:
                list[j] = list[j-gap]
                j -= gap
            list [j] = temp
        gap //= 2
    return list

# Batasan nilai yang diambil yaitu antara 200 sampai 800 serta 
#mendapatkan angka-angka acak yang berjumlah 12 elemen
arr = [random.randint(200,800) for i in range(12)]

print (90*"=")
print(f"|| Shell sort belum urut : {arr}")
shell(arr)
print(F"|| Shell sort terurut : {arr}")

################################################################################################################################################