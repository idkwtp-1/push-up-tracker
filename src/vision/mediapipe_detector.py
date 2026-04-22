import cv2
import mediapipe as mp
import time
import numpy as np
from .detector_base import BaseDetector
from src.utils.helpers import calculate_angle

class MediaPipeDetector(BaseDetector):
    def __init__(self):
        super().__init__()
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(min_detection_confidence=0.7, min_tracking_confidence=0.7)
        self.mp_draw = mp.solutions.drawing_utils
        self.reset()

    def reset(self):
        self.in_pushup_position = False
        self.down_position_time = None
        self.baseline_angle = 160
        self.history = []

    def process(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.pose.process(rgb)
        
        event = None
        status = "POSITIONING..."
        
        if results.pose_landmarks:
            self.mp_draw.draw_landmarks(frame, results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS)
            lm = results.pose_landmarks.landmark
            
            # Key points
            h, w, _ = frame.shape
            try:
                shoulder = [lm[11].x * w, lm[11].y * h]
                elbow = [lm[13].x * w, lm[13].y * h]
                wrist = [lm[15].x * w, lm[15].y * h]
                
                angle = calculate_angle(shoulder, elbow, wrist)
                cv2.putText(frame, str(int(angle)), (int(elbow[0]), int(elbow[1])), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                
                if angle < 95:
                    if not self.in_pushup_position:
                        self.in_pushup_position = True
                        self.down_position_time = time.time()
                    status = "DOWN"
                elif angle > 160:
                    if self.in_pushup_position:
                        if time.time() - self.down_position_time > 0.3:
                            event = 'up'
                            status = "UP!"
                        self.in_pushup_position = False
                    else:
                        status = "READY"
            except:
                pass
                
        return frame, event, status
