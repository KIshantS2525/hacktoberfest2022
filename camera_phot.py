import cv2
cam = cv2.VideoCapture(0)
result, image = cam.read()
if result:
	cv2.imshow("Camera photo", image)
	cv2.imwrite("python click.png", image)
	waitKey(0)
	cv2.destroyAllWindows
else:
	print("No image detected. Please! try again")
