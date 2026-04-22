import threading
import time
import cv2
import os
from flask import Flask, Response, jsonify, send_from_directory
from src.core.data_manager import DataManager
from src.vision.mediapipe_detector import MediaPipeDetector
from src.vision.contour_detector import ContourDetector

app = Flask(__name__, static_folder='../web')
data_manager = DataManager()
state = {'pushups': 0, 'status': 'READY', 'started': False, 'goal_reached': False}
lock = threading.Lock()
_latest_frame = None

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory(app.static_folder, path)

@app.route('/video_feed')
def video_feed():
    def gen():
        while True:
            with lock:
                if _latest_frame is None: continue
                yield (b'--frame
Content-Type: image/jpeg

' + _latest_frame + b'
')
            time.sleep(0.03)
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/api/status')
def get_status():
    return jsonify(state)

@app.route('/api/start', methods=['POST'])
def start_session():
    state['started'] = True
    state['pushups'] = 0
    return jsonify({'status': 'ok'})

@app.route('/api/history')
def get_history():
    return jsonify(data_manager.get('pushup_history', []))

@app.route('/api/mock_video', methods=['POST'])
def mock_video():
    idx = data_manager.get_next_video_index()
    vids = [
        'WhatsApp Video 2026-04-19 at 13.42.47.mp4',
        'WhatsApp Video 2026-04-19 at 13.42.48.mp4',
        'WhatsApp Video 2026-04-19 at 13.42.48 (1).mp4'
    ]
    return jsonify({'video': vids[idx]})

class PushUpTrackerApp:
    def run(self):
        threading.Thread(target=self.camera_worker, daemon=True).start()
        app.run(port=5000, threaded=True)

    def camera_worker(self):
        global _latest_frame
        cap = cv2.VideoCapture(0)
        detector = MediaPipeDetector()
        while True:
            ret, frame = cap.read()
            if not ret: continue
            
            frame, event, status = detector.process(frame)
            if event == 'up' and state['started']:
                state['pushups'] += 1
                if state['pushups'] >= 100: state['goal_reached'] = True
            
            state['status'] = status
            
            _, buffer = cv2.imencode('.jpg', frame)
            with lock:
                _latest_frame = buffer.tobytes()
