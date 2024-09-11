import cv2

#
img = cv2.imread("pexels-thatguycraig000-1563356.jpg")
print("Resim boyutu: ", img.shape)
cv2.imshow("Orijinal",img)

# resized
imgResized = cv2.resize(img, (800,800))
print("Resized Img Shape: ", imgResized.shape)
cv2.imshow("Img Resized: ",imgResized)

# kırp
imgCropped = img[:200,0:300] # widht height --> height widht
cv2.imshow("Kirpilan Resim: ", imgCropped)


























