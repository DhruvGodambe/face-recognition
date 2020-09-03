import cv2
import face_recognition

imgObama = face_recognition.load_image_file('./real obama.jpeg')
imgObama = cv2.cvtColor(imgObama, cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('./obama test.jpg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgObama)[0]
encodeObama = face_recognition.face_encodings(imgObama)[0]
cv2.rectangle(imgObama, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255,0,0), 2)

faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255,0,0), 2)

results = face_recognition.compare_faces([encodeObama], encodeTest)
print(results)

cv2.imshow('Barack Obama', imgObama)
cv2.imshow('Test Obama', imgTest)
cv2.waitKey(0)