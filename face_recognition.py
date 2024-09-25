import cv2
import face_recognition

#person_dhanin
img = cv2.imread(r"D:\face regconition\dhanin.jpg")
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_encoding = face_recognition.face_encodings(rgb_img)[0]


#person_tarun
img2 = cv2.imread(r"D:\face regconition\other_persons\tarun.jpg")
rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
img_encoding2 = face_recognition.face_encodings(rgb_img2)[0]

result = face_recognition.compare_faces([img_encoding], img_encoding2)
print("Result : ", result)
if(result==[True]):
    print("same member")
else:
    print("not same member")
cv2.imshow("img",img)
cv2.imshow("img2",img2)
cv2.waitKey(0)