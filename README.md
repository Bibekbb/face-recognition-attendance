# Face Recognition Attendance System  

A real-time face recognition-based attendance system using OpenCV, KNN classifier, and Haar cascades. The system captures live video feed, detects faces, and records attendance in a CSV file with the timestamp.

---

## Features  
- **Face Detection**: Uses Haar Cascade Classifier to detect faces from live video feed.  
- **Face Recognition**: Implements K-Nearest Neighbors (KNN) to recognize faces from the dataset.  
- **Attendance Logging**: Automatically logs recognized faces with the current time into a CSV file.  
- **Voice Feedback**: Announces attendance logging using the SAPI voice engine (Windows only).  

---

## Prerequisites  
Ensure the following are installed:  

- Python 3.x  
- OpenCV  
- NumPy  
- Scikit-learn  
- Pickle  
- PyWin32 (for voice feedback)  

---

## Installation  

1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/face-recognition-attendance.git
   cd face-recognition-attendance
   ```  

2. Install required dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  

3. Create a directory structure:  
   ```plaintext
   data/
       haarcascade_frontalface_default.xml
       faces_data.pkl
       names.pkl
   Attendance/
   background.png
   ```  

4. Add the `haarcascade_frontalface_default.xml` file in the `data/` directory.  

---

## Usage  

### Step 1: Register Faces  
1. Run the face registration script:  
   ```bash
   python register_faces.py
   ```  
2. Enter the name when prompted.  
3. The script will capture 100 face images and save them to `data/faces_data.pkl` and `data/names.pkl`.  

### Step 2: Start Attendance System  
1. Run the main script:  
   ```bash
   python attendance_system.py
   ```  
2. Point the camera at registered individuals.  
3. Press **`o`** to log attendance.  
4. Press **`q`** to exit the system.  

### Step 3: View Attendance Logs  
Check the `Attendance/` directory for daily CSV files named as `Attendance_<date>.csv`.  

---

## Folder Structure  
```plaintext
face-recognition-attendance/
│
├── Attendance/  
│   ├── Attendance_<date>.csv
│ 
├── data/  
│   ├── haarcascade_frontalface_default.xml  
│   ├── faces_data.pkl  
│   ├── names.pkl   
│
├── app.py
├── faces_data.py  
├── attendance_system.py  
├── background-img.png  
├── requirements.txt  
├── README.md  
```  

---

## How It Works  
1. **Face Registration**:  
   - Captures images from the webcam.  
   - Preprocesses and saves the data for training.  

2. **Face Recognition**:  
   - Detects faces in real-time using Haar cascades.  
   - Recognizes faces using the KNN classifier.  

3. **Attendance Logging**:  
   - Matches detected faces with the dataset.  
   - Logs attendance in a daily CSV file with the timestamp.  

---

## Dependencies  
- OpenCV  
- NumPy  
- Scikit-learn  
- Pickle  
- PyWin32  

Install them using the `requirements.txt` file:  
```bash
pip install -r requirements.txt
```  

---

## Contributions  
Feel free to fork this repository and create pull requests for improvements.  

---

## License  
This project is licensed under the MIT License.  

---

## Acknowledgments  
- OpenCV for computer vision functionalities.  
- Scikit-learn for the KNN classifier.  
- Haar cascades for face detection.  
- PyWin32 for voice feedback.  

**Happy Coding!** 😊