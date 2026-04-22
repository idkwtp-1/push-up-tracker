import cv2
import numpy as np
import time
from .detector_base import BaseDetector

class ContourDetector(BaseDetector):
    def __init__(self):
        super().__init__()
        self.bg_subtractor = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=50)
        self.nose_y_baseline = None
        self.calibration_frames = 0
        self.pushup_state = 'idle'
        self.min_displacement = 0.04

    def reset(self):
        self.nose_y_baseline = None
        self.calibration_frames = 0
        self.pushup_state = 'idle'

    def process(self, frame):
        h, w = frame.shape[:2]
        fg_mask = self.bg_subtractor.apply(frame)
        contours, _ = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        event = None
        status = "READY"
        
        if contours:
            largest = max(contours, key=cv2.contourArea)
            if cv2.contourArea(largest) > 5000:
                x, y, w_c, h_c = cv2.boundingRect(largest)
                head_y = y
                
                if self.calibration_frames < 30:
                    self.calibration_frames += 1
                    status = "CALIBRATING..."
                elif self.nose_y_baseline is None:
                    self.nose_y_baseline = head_y
                else:
                    diff = (head_y - self.nose_y_baseline) / h
                    if diff > self.min_displacement and self.pushup_state != 'down':
                        self.pushup_state = 'down'
                        status = "DOWN"
                    elif diff < 0.01 and self.pushup_state == 'down':
                        self.pushup_state = 'up'
                        event = 'up'
                        status = "UP!"
        
        return frame, event, status
