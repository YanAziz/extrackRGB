# cv2 as cv: Library OpenCV yang diimpor dengan alias cv untuk memudahkan pemanggilan fungsi.
# matplotlib.pyplot as plt: Library Matplotlib yang digunakan untuk menampilkan gambar dan histogram.
import cv2 as cv
import matplotlib.pyplot as plt

# cv.imread() digunakan untuk membaca gambar dari file. 
# Parameter pertama "cat.jpg" menentukan file gambar yang akan dibaca. 
# Parameter kedua cv.IMREAD_GRAYSCALE menentukan bahwa gambar akan dibaca dalam mode grayscale.
I = cv.imread("cat.jpg", cv.IMREAD_GRAYSCALE)

# cv.equalizeHist() digunakan untuk melakukan equalisasi histogram pada gambar grayscale. 
# Ini akan meningkatkan kontras gambar dengan meratakan distribusi intensitas pikselnya.
equ = cv.equalizeHist(I)

# Menggunakan plt.figure() untuk membuat figur baru dengan ukuran yang ditentukan.
# Menggunakan plt.subplot() untuk menambahkan subplot di dalamnya. 
# Subplot pertama menampilkan gambar asli, dan subplot kedua menampilkan gambar setelah equalization.
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(I, cmap='gray')
plt.title('Gambar Asli')

plt.subplot(1, 3, 2)
plt.imshow(equ, cmap='gray')
plt.title('Gambar Setelah Equalization')

# Menggunakan plt.hist() untuk menghitung dan menampilkan histogram piksel dari gambar asli dan gambar setelah equalization.
# plt.legend() digunakan untuk menambahkan legenda pada plot untuk membedakan histogram gambar asli dan setelah equalization.
plt.subplot(1, 3, 3)
plt.hist(I.flatten(), 256, [0,256], color='r', alpha=0.5)
plt.hist(equ.flatten(), 256, [0,256], color='g', alpha=0.5)
plt.legend(('Histogram Asli', 'Histogram Setelah Equalization'))

# plt.show() digunakan untuk menampilkan keseluruhan plot yang telah dibuat. 
# Ini akan menampilkan gambar asli, gambar setelah equalization, dan histogramnya dalam satu jendela tampilan.
plt.show()