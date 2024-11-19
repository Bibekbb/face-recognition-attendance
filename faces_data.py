import cv2
import pickle
import numpy as np
import os

video_capture = cv2.VideoCapture(0)
face_detector = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

collected_faces = []
frame_counter = 0

user_name = input("Enter Your Name: ")

while True:
    ret, frame = video_capture.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detected_faces = face_detector.detectMultiScale(gray_frame, 1.3, 5)

    for (x, y, w, h) in detected_faces:
        cropped_face = frame[y:y+h, x:x+w, :]
        resized_face = cv2.resize(cropped_face, (50, 50))
        
        if len(collected_faces) <= 100 and frame_counter % 10 == 0:
            collected_faces.append(resized_face)
        
        frame_counter += 1
        cv2.putText(frame, str(len(collected_faces)), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 1)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 1)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == ord('q') or len(collected_faces) == 100:
        break

video_capture.release()
cv2.destroyAllWindows()

collected_faces = np.asarray(collected_faces)
collected_faces = collected_faces.reshape(100, -1)

if 'names.pkl' not in os.listdir('data/'):
    user_names = [user_name] * 100
    with open('data/names.pkl', 'wb') as file:
        pickle.dump(user_names, file)
else:
    with open('data/names.pkl', 'rb') as file:
        user_names = pickle.load(file)
    user_names = user_names + [user_name] * 100
    with open('data/names.pkl', 'wb') as file:
        pickle.dump(user_names, file)

if 'faces_data.pkl' not in os.listdir('data/'):
    with open('data/faces_data.pkl', 'wb') as file:
        pickle.dump(collected_faces, file)
else:
    with open('data/faces_data.pkl', 'rb') as file:
        existing_faces = pickle.load(file)
    existing_faces = np.append(existing_faces, collected_faces, axis=0)
    with open('data/faces_data.pkl', 'wb') as file:
        pickle.dump(existing_faces, file)
