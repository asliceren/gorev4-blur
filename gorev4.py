import cv2
import numpy as np

image = cv2.imread("gurultulu_resim.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    print("Hata: Resim bulunamadi!")
    exit()

h, w = image.shape

opencv_sonuc = cv2.blur(image, (3, 3))
cv2.imwrite("filtreli_opencv.jpg", opencv_sonuc)

manuel_sonuc = np.zeros((h, w), dtype=np.uint8)

for y in range(1, h - 1):
    for x in range(1, w - 1):
        komsuluk = image[y - 1:y + 2, x - 1:x + 2]
        ortalama = np.sum(komsuluk) // 9
        manuel_sonuc[y, x] = ortalama

manuel_sonuc[0, :] = image[0, :]
manuel_sonuc[h - 1, :] = image[h - 1, :]
manuel_sonuc[:, 0] = image[:, 0]
manuel_sonuc[:, w - 1] = image[:, w - 1]

cv2.imwrite("filtreli_manuel.jpg", manuel_sonuc)
print("Islem tamamlandi!")

cv2.imshow("1. Gurultulu Resim", image)
cv2.imshow("2. OpenCV Blur", opencv_sonuc)
cv2.imshow("3. Manuel Konvolusyon", manuel_sonuc)

cv2.waitKey(0)
cv2.destroyAllWindows()
