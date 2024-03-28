# Import Library: Import library OpenCV dan NumPy.
# OpenCV (cv2) adalah library yang umum digunakan untuk pengolahan citra digital,
#   sementara NumPy (np) digunakan untuk operasi numerik.
import cv2
import numpy as np

# Membaca Gambar: Membaca gambar dari file "cat.jpg" menggunakan fungsi cv2.imread(). 
# Gambar ini akan disimpan dalam variabel image.
image_origin = cv2.imread("cat.jpg")

# Shape digunakan untuk mendapatkan dimensi gambar, yaitu tinggi, lebar, dan 
# channel warna (misalnya RGB memiliki 3 channel).
height, width, dimen = image_origin.shape

# Digunakan untuk membuat array nol dengan ukuran yang sama dengan gambar asli, dengan 
# tipe data unsigned integer 8-bit (uint8). 
# Ini akan digunakan untuk menyimpan citra keabuan (grayscale).
copy_image = np.zeros((height, width), dtype=np.uint8)

# Dilakukan iterasi pada setiap pixel dalam gambar asli.
# Setiap nilai pixel dalam gambar konversi dihitung menggunakan formula konversi 
# warna keabuan yang umum : 0.299 * R + 0.587 * G + 0.114 * B
for i in range(height):
    for j in range(width):
        copy_image[i, j] = (image_origin[i, j, 0] * 0.299) + (image_origin[i, j, 1] * 0.587) + (image_origin[i, j, 2] * 0.114)

# Fungsi cv2.imshow() digunakan untuk menampilkan gambar. Parameter pertama adalah 
# judul jendela, dan parameter kedua adalah gambar yang akan ditampilkan.
cv2.imshow("grayscale", copy_image)

# Fungsi cv2.resize() digunakan untuk mengubah ukuran gambar ke ukuran yang diinginkan 
# (dalam hal ini, 400x500 piksel).
img_resize = cv2.resize(image_origin, (400, 500))

# Menampilkan gambar asli dan gambar yang diubah ukurannya.
cv2.imshow("Original", image_origin)
cv2.imshow("img_resize", img_resize)

# Membuat matriks dengan semua elemen bernilai 60 (menambahkan kecerahan gambar).
incr_matrix = np.ones(image_origin.shape, dtype="uint8") * 60

# Menggunakan fungsi cv2.add() untuk menambahkan matriks ini ke gambar asli, sehingga meningkatkan kecerahan gambar.
brightened_image = cv2.add(image_origin, incr_matrix)

# Menggunakan fungsi cv2.subtract() untuk mengurangi matriks kecerahan dari gambar asli, 
# sehingga mengurangi kecerahan gambar.
darkened_image = cv2.subtract(image_origin, incr_matrix)

# Menampilkan gambar yang telah ditingkatkan dan diperburuk kecerahannya.
cv2.imshow("Brightened", brightened_image)
cv2.imshow("Darkened", darkened_image)

# cv2.waitKey(0) digunakan untuk menunggu penekanan tombol apa pun dari keyboard.
# cv2.destroyAllWindows() digunakan untuk menutup semua jendela tampilan gambar setelah sebuah tombol ditekan.
cv2.waitKey(0)
cv2.destroyAllWindows()