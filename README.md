# 🏋️‍♂️ Push-Up Tracker 100

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0-lightgrey?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-Pose-green?logo=google&logoColor=white)](https://mediapipe.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A high-performance Windows desktop application that uses **AI-powered pose detection** to track your push-ups in real-time. Designed to help you smash the **100-rep daily goal** with a premium, glassmorphism-styled interface.

---

## ✨ Key Features

*   🤖 **AI Pose Detection:** Powered by MediaPipe for high-accuracy tracking.
*   🕒 **Time-Freedom Conversion:** 1 push-up = 1 minute of "freedom" (tracked via the UI).
*   🔒 **Goal Lock:** The interface remains focused until you reach your daily 100 reps.
*   📈 **Workout History:** Visualized progress using Chart.js to track your fastest times.
*   🎙️ **Voice Commands:** Offline speech recognition (Vosk) to control the session hands-free.
*   🐱 **Early-Exit Penalty:** Quitting early (1-99 reps) triggers a sequence of "distraction" cat videos!

## 🚀 Tech Stack

| Layer | Technology |
| :--- | :--- |
| **Backend** | Flask (Python) |
| **Vision** | MediaPipe Pose & OpenCV |
| **Frontend** | HTML5, CSS3 (Vanilla), JavaScript |
| **Windowing** | PyWebview (Native Window) |
| **Speech** | Vosk (Offline recognition) |
| **Data** | JSON Persistence |

## 🛠️ Installation & Setup

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/idkwtp-1/push-up-tracker.git
    cd push-up-tracker
    ```

2.  **Install Dependencies:**
    Run the provided batch file:
    ```bash
    install.bat
    ```

3.  **Download Models:**
    *   Place the `vosk-model-small-en-us-0.15` directory in the root.
    *   The MediaPipe `pose_landmarker.task` will auto-download on first run.

4.  **Add Media:**
    *   Place 3 `.mp4` files in `src/cat_vids/` (see tracker.py for specific filenames).

## 🏃‍♂️ Usage

Simply double-click `start_pushup_tracker.bat` to launch the app.
*   The camera will initialize automatically.
*   Maintain a "plank" position to start detection.
*   Reach 100 reps to unlock the full history and completion stats!

---

*Made with ❤️ for a healthier lifestyle.*