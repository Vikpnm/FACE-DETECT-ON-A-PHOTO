import cv2
import os

source_folder = "source"
result_folder = "result"
old_folder = "old"

if not os.path.exists(result_folder):
    os.makedirs(result_folder)
if not os.path.exists(old_folder):
    os.makedirs(old_folder)
for filename in os.listdir(source_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image_path = os.path.join(source_folder, filename)
        image = cv2.imread(image_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        result_image_path = os.path.join(result_folder, filename)
        cv2.imwrite(result_image_path, image)
        old_image_path = os.path.join(old_folder, filename)
        os.rename(image_path, old_image_path)
print("detection completed.")
