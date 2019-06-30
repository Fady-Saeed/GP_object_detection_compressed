import obj
import cv2 

frame = cv2.imread("./image.jpg")


obj.init()
data = obj.process(frame)
frame = obj.draw(frame, data)
obj.finish()

cv2.imshow("", frame)
cv2.waitKey()