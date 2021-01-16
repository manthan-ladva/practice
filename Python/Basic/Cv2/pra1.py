import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


img = cv2.imread("photo.jpg")
#gray_img = cv2.cvtColor(img, (cv2.COLOR_RGB2GRAY))

faces = face_cascade.detectMultiScale(img,
scaleFactor = 1.5,
minNeighbors = 5)


for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x+w,  y+h), (255, 0, 255), 5)

print(type(faces))
print(faces)
print(img.shape)

resized = cv2.resize(img, (int(img.shape[0]/3), int(img.shape[1]/3)))

cv2.imshow("Gray", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()