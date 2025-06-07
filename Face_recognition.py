import cv2
import dlib

#gán biến đọc file
img = cv2.imread("/Users/cuong/Desktop/ai recognition/Nguoiphanxu.jpg")

#đổi ảnh màu thành ảnh trắng đen
gray = cv2.cvtColor(src = img, code = cv2.COLOR_BGR2GRAY)

#dùng dlib nhận diện khuôn mặt
face_detector= dlib.get_frontal_face_detector()

#nhận diện khuôn mặt trong ảnh
faces = face_detector(gray)

#loop tọa độ vẽ hình trên ảnh
for face in faces:
    x1 = face.left()
    x2 = face.right()
    y1 = face.top()
    y2 = face.bottom()
    
    cv2.rectangle(img = img, pt1 = (x1,y1), pt2 = (x2,y2), color = (0,255,0), thickness=3)
    
cv2.imshow(winname = "Face Recognition App", mat = img)
#ấn key bất kỳ để tắt cửa sổ
cv2.waitKey(delay = 0)
cv2.destroyAllWindows()
