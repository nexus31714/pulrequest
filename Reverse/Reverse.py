
#img[x,y] = abs(img[x,y] - 255)


 #   for x in np.nditer(imagem, op_flags=['readwrite']):
    #    x = abs(x - 255)
   # cv2.imwrite(name, imagem)

    #def inverte(imagem, name):
     #   imagem = (255 - imagem)
      #  cv2.imwrite(name, imagem)

import cv2


def OpenCV_Access_RGBValue(inMat):

    h = inMat.shape[0]
    w = inMat.shape[1]

    #eb = 0
    #for y in range(0, h):
    #    for x in range(0, w):
    #        if any(inMat[x, y]>eb):
    #            eb=inMat[x,y]



    for y in range(0, h):
        for x in range(0, w):

            b = inMat[y, x, 0]
            g = inMat[y, x, 1]
            r = inMat[y, x, 2]

            #b = eb - b
            #g = eb - g
            #r = eb - r

            b = 256 - b
            g = 256 - g
            r = 256 - r



            inMat[y, x, 0] = b
            inMat[y, x, 1] = g
            inMat[y, x, 2] = r


    return inMat



inMat = cv2.imread("img.jpg")

OpenCV_Access_RGBValue(inMat)

cv2.namedWindow('test', 0)
cv2.imwrite('output.jpg', inMat)
cv2.imshow('test', inMat)
cv2.waitKey(0)

#manuel histogram hesaplama
histogramDizisi = np.zeros(256) #Histogram hesabı için 0 'lardan oluşan boş bir dizi oluşturdum.
yukseklik,genislik=kartalResmi.shape #Görüntünün boyutları alındı çünkü for döngüsünde sınırları belirlememiz gerekiyordu.

for i in range(yukseklik):
    for j in range(genislik):
        pikselDegeri=kartalResmi[i][j] #Görüntünün  piksel değerleri sıra ile alındı.
        histogramDizisi[pikselDegeri]= histogramDizisi[pikselDegeri] + 1 #okunan değerin index ine gidilip 1 artırıldı.


np.set_printoptions(suppress=True) #histogram dizisini yazdırırken üst biçiminde yazıyordu onu engellemek için yapıldı.Örn:2.97351e+05  nin yerine 297351 yazımı gibi daha saegözükmesi için

print(histogramDizisi)
print("\nHistogram dizisinin en çok tekrar eden değeri: ",np.max(histogramDizisi))


cv2.waitKey()
