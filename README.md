# Facial Attendance System

## Overview

The **Facial Attendance System** is a Python-based application that uses facial recognition to automate attendance tracking. It leverages machine learning with k-Nearest Neighbors (kNN), OpenCV for face detection, and Streamlit for web-based data visualization.

---

## Features

- **Real-time Facial Recognition**: Detect and recognize faces from a live webcam feed.
- **Attendance Logging**: Automatically logs attendance with name and timestamp into a CSV file.
- **Streamlit Integration**: View attendance data directly in a web interface.
- **Storage Management**: Stores face data for multiple users using pickle files for easy access and retrieval.

---

## Technologies Used

- **Python**: Core programming language.
- **OpenCV**: For face detection and image processing.
- **Streamlit**: For web-based visualization.
- **scikit-learn**: Machine learning library for classification.
- **pickle**: For saving and loading face data and labels.
- **Win32com**: For text-to-speech functionality on Windows.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Bibekbb/face-recognition-attendance.git
   cd facial-attendance-system
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Place the required files in the `data/` folder:
   - `haarcascade_frontalface_default.xml`
   - `names.pkl`
   - `faces_data.pkl`

---

## How to Run

### Real-Time Facial Recognition
1. Run the real-time face detection script:
   ```bash
   python face_recognition.py
   ```
2. Press `o` to log attendance or `q` to quit the application.

### Viewing Attendance
1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```
2. Upload the attendance CSV file to view data.

---

## Folder Structure

```
facial-attendance-system/
│
├── data/                  
├── Attendance/            
├── app.py                 
├── background-img.png     
├── face_data.py
├── attendance_system.py
├── requirements.txt       
└── README.md              
```

---

## Contributing

Contributions are welcome! Fork the repository and submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- OpenCV team for their robust computer vision library.
- Scikit-learn for powerful machine learning tools.
- Streamlit for easy-to-build web apps.
 
**Happy Coding!** 😊
