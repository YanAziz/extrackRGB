# Iqyan Aziz Syamaidzar
# 2203040066
# Pengolahan Citra Digital C1
# ELINDRA AMBAR PAMBUDI, S.T., M.KOM

# Extraction of RGB from an image

# Import Library: Import library OpenCV dan NumPy. 
# OpenCV (cv2) adalah library yang umum digunakan untuk pengolahan citra digital, 
#   sementara NumPy (np) digunakan untuk operasi numerik.
import cv2 as cv
import numpy as np

# Membaca Gambar: Membaca gambar dari file "cat.jpg" menggunakan fungsi cv.imread(). 
# Gambar ini akan disimpan dalam variabel image.
# Menampilkan Gambar Asli: Menampilkan gambar yang telah dibaca menggunakan fungsi cv.imshow(). 
# Judul jendela akan menjadi "This is a image".
image = cv.imread("cat.jpg")
cv.imshow("This is a image", image)

# Mengambil Kanal Warna: Memisahkan gambar menjadi tiga kanal warna: 
#   merah (R), hijau (G), dan biru (B) menggunakan fungsi cv.split(). 
# Setiap kanal warna akan disimpan dalam variabel terpisah, yaitu r, g, dan b.
r,g,b = cv.split(image)

# Membuat Citra Kosong: Membuat citra kosong yang memiliki ukuran yang sama dengan citra asli. 
# Citra kosong ini digunakan untuk menghasilkan citra tunggal dengan satu kanal warna tertentu.
blank = np.zeros(image.shape[:2],dtype="uint8")

# Extract Red
# Menggabungkan Kanal Merah: Menggabungkan kanal warna merah r dengan dua kanal warna kosong (blank). 
# Hasilnya adalah citra dengan hanya warna merah yang terlihat.
red = cv.merge([r,blank,blank])

# Extract Green 
# Menggabungkan Kanal Hijau: Menggabungkan kanal warna hijau g dengan dua kanal warna kosong (blank). 
# Hasilnya adalah citra dengan hanya warna hijau yang terlihat.
green = cv.merge([blank,g,blank])

# Extract Blue 
# Menggabungkan Kanal Biru: Menggabungkan kanal warna biru b dengan dua kanal warna kosong (blank). 
# Hasilnya adalah citra dengan hanya warna biru yang terlihat.
blue = cv.merge([blank,blank,b])

# Menampilkan Gambar Hasil: Menampilkan gambar dengan hanya satu kanal warna pada setiap jendela yang berbeda. 
# Terdapat tiga jendela yang menampilkan warna merah, hijau, dan biru secara terpisah.
cv.imshow("This is red image", red)
cv.imshow("This is green image", green)
cv.imshow("This is blue image", blue)

# Menunggu Tombol Keyboard Ditekan: Menunggu pengguna menekan tombol keyboard untuk menutup semua jendela gambar. 
# Fungsi cv.waitKey(0) akan memblok eksekusi hingga pengguna menekan tombol keyboard.
cv.waitKey(0)
