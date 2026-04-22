# Push-Up Tracker

A Windows-based computer vision application designed for real-time push-up tracking and daily goal management. This project utilizes MediaPipe for pose estimation and a Flask-based MJPEG streaming architecture to provide a native-feeling desktop experience.

[![GitHub license](https://img.shields.io/github/license/idkwtp-1/push-up-tracker)](https://github.com/idkwtp-1/push-up-tracker/blob/main/LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)

## Overview

Push-Up Tracker is an automated workout assistant that ensures exercise form integrity and session persistence. It converts physical effort into "Freedom Minutes," providing a gamified yet rigorous approach to reaching a 100-rep daily milestone.

## Technical Architecture

*   **Vision Engine:** MediaPipe Pose Landmarker (Heavy Model) for primary detection, with a Haar Cascade + Contour detection fallback for lower-spec hardware.
*   **Backend:** Python/Flask serving as a REST API and MJPEG video provider.
*   **UI/UX:** A glassmorphism-inspired web interface rendered via `pywebview` for a standalone desktop application feel.
*   **Speech Integration:** Offline voice recognition using the Vosk engine for hands-free session control.
*   **Data Persistence:** Local JSON-based storage for workout history and performance metrics (Fastest 100).

## Installation

### Prerequisites
*   Windows OS (Required for `winsound` and `winreg` integrations)
*   Python 3.8 or higher
*   Webcam

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/idkwtp-1/push-up-tracker.git
   ```
2. Install dependencies:
   ```bash
   ./install.bat
   ```
3. Configure models:
   *   The MediaPipe model (`pose_landmarker.task`) downloads automatically on initialization.
   *   Download and extract the `vosk-model-small-en-us-0.15` directory into the project root.

## Usage

Launch the application using the provided batch file:
```bash
./start_pushup_tracker.bat
```

### Key Controls
*   **Calibration:** The system automatically calibrates your "plank" position upon session start.
*   **Voice:** Say "Stop" after reaching the 100-rep goal to safely terminate the session.
*   **Early Exit:** Quitting before the 100-rep goal will trigger a sequence of mock playback videos.

## Roadmap
- [ ] Integration with external fitness APIs.
- [ ] Multi-exercise support (Squats, Pull-ups).
- [ ] Advanced form correction feedback using joint angle analysis.

---
*Developed for personal performance tracking and computer vision research.*