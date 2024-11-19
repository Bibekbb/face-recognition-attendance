from sklearn.neighbors import KNeighborsClassifier
import cv2
import pickle
import numpy as np
import os
import csv
import time
from datetime import datetime
from win32com.client import Dispatch

def speak(message):
    speaker = Dispatch("SAPI.SpVoice")
    speaker.Speak(message)

video_capture = cv2.VideoCapture(0)
face_detector = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

with open('data/names.pkl', 'rb') as name_file:
    label_data = pickle.load(name_file)
with open('data/faces_data.pkl', 'rb') as face_file:
    face_data = pickle.load(face_file)

print('Shape of Face Data Matrix --> ', face_data.shape)

knn_classifier = KNeighborsClassifier(n_neighbors=5)
knn_classifier.fit(face_data, label_data)

background_image = cv2.imread("background-img.png")

csv_columns = ['NAME', 'TIME']

while True:
    ret, frame = video_capture.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detected_faces = face_detector.detectMultiScale(gray_frame, 1.3, 5)
    
    for (x, y, w, h) in detected_faces:
        cropped_face = frame[y:y+h, x:x+w, :]
        resized_face = cv2.resize(cropped_face, (50, 50)).flatten().reshape(1, -1)
        predicted_label = knn_classifier.predict(resized_face)
        
        current_time = time.time()
        current_date = datetime.fromtimestamp(current_time).strftime("%d-%m-%Y")
        current_timestamp = datetime.fromtimestamp(current_time).strftime("%H:%M-%S")
        
        attendance_file_exists = os.path.isfile(f"Attendance/Attendance_{current_date}.csv")
        
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 1)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 2)
        cv2.rectangle(frame, (x, y-40), (x+w, y), (50, 50, 255), -1)
        cv2.putText(frame, str(predicted_label[0]), (x, y-15), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)
        
        attendance_entry = [str(predicted_label[0]), str(current_timestamp)]

    background_image[162:162 + 480, 55:55 + 640] = frame
    cv2.imshow("Frame", background_image)
    
    key_press = cv2.waitKey(1)
    
    if key_press == ord('o'):
        speak("Attendance Taken.")
        time.sleep(5)
        if attendance_file_exists:
            with open(f"Attendance/Attendance_{current_date}.csv", "a") as attendance_file:
                writer = csv.writer(attendance_file)
                writer.writerow(attendance_entry)
        else:
            with open(f"Attendance/Attendance_{current_date}.csv", "a") as attendance_file:
                writer = csv.writer(attendance_file)
                writer.writerow(csv_columns)
                writer.writerow(attendance_entry)

    if key_press == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
