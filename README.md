# 🚗 Driver Drowsiness Detection System

A real-time AI-based system that detects driver drowsiness using computer vision and alerts the user to prevent potential accidents.

---

## 📌 Overview

Driver fatigue is one of the leading causes of road accidents. This project presents a real-time solution that monitors eye movements using facial landmarks and detects drowsiness based on Eye Aspect Ratio (EAR). When prolonged eye closure is detected, the system triggers an alert to wake the driver.

---

## 🔥 Features

- 🎥 Real-time face and eye tracking  
- 👁️ Eye Aspect Ratio (EAR) based detection  
- 🚨 Instant audio alert system  
- 🌐 Flask-based web application  
- 📊 Live status display (Awake / Drowsy)  
- ⚡ Optimized for real-time performance  

---

## 🛠️ Tech Stack

- **Programming Language:** Python  
- **Computer Vision:** OpenCV  
- **Face Detection:** MediaPipe Face Mesh  
- **Web Framework:** Flask  
- **Audio Alert:** Pygame  
- **Math & Utilities:** NumPy, SciPy  

---

## 🧠 How It Works

1. Captures live video using webcam  
2. Detects facial landmarks using MediaPipe  
3. Extracts eye coordinates  
4. Computes Eye Aspect Ratio (EAR)  
5. Monitors EAR over consecutive frames  
6. If EAR remains below threshold → detects drowsiness  
7. Triggers alert sound and visual warning  

---

## 📂 Project Structure


Driver-Drowsiness/
│
├── app.py # Flask application
├── detector.py # Detection logic
├── requirements.txt # Dependencies
│
├── static/
│ └── alarm.mp3 # Alert sound
│
├── templates/
│ └── index.html # Web UI
│
└── README.md


---

## 🚀 Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/Driver-Drowsiness-Detection.git
cd Driver-Drowsiness-Detection
2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Run the application
python app.py
5️⃣ Open in browser
http://127.0.0.1:5000/
🎥 Demo

📌 Add your demo video or screenshots here
(Recorded using OBS Studio)

⚙️ Configuration

You can adjust detection sensitivity in detector.py:

EAR_THRESHOLD = 0.20
FRAME_CHECK = 10
🚀 Future Improvements
📊 Fatigue scoring system
📱 Mobile app integration
☁️ Cloud-based deployment
🧠 Deep learning-based eye classification
📈 Dashboard analytics
🤝 Contributing

Contributions are welcome! Feel free to fork this repository and submit pull requests.

📜 License

This project is open-source and available under the MIT License.

⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub!

👨‍💻 Author

Tanishq Agrawal
Aspiring Machine Learning Engineer 🚀
