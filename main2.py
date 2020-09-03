import cv2
import face_recognition

inputImage = face_recognition.load_image_file('./me.jpg')
inputImage = cv2.cvtColor(inputImage, cv2.COLOR_BGR2RGB)

cap = cv2.VideoCapture(0)

faceLoc = face_recognition.face_locations(inputImage)[0]
encodeObama = face_recognition.face_encodings(inputImage)[0]
cv2.rectangle(inputImage, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255,0,0), 2)

while True:
	_, imgTest = cap.read()
	# imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

	faceLocTest = face_recognition.face_locations(imgTest)
	encodeTest = face_recognition.face_encodings(imgTest)

	if len(faceLocTest) > 0:
		cv2.rectangle(imgTest, (list(faceLocTest[0])[3], list(faceLocTest[0])[0]), (list(faceLocTest[0])[1], list(faceLocTest[0])[2]), (255,0,0), 2)

		results = face_recognition.compare_faces(encodeObama, encodeTest)
		if results[0] == True:
			cv2.putText(imgTest, 'Dhruv Godambe', (list(faceLocTest[0])[3], list(faceLocTest[0])[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
		else:
			cv2.putText(imgTest, 'unkown person', (list(faceLocTest[0])[3], list(faceLocTest[0])[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

	cv2.imshow('Reference image', inputImage)
	cv2.imshow('Test cam', imgTest)
	if cv2.waitKey(1) & 0xff == ord('q'):
		break