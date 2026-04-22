import cv2

class BaseDetector:
    def __init__(self):
        self.is_tracking = False

    def process(self, frame):
        """Process the frame and return (processed_frame, pushup_event, status_msg)"""
        return frame, None, ""

    def reset(self):
        pass
