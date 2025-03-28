import cv2
import torch
from ultralytics import YOLO

class FallDetection:
    def __init__(self, model_path="D:/UNI/FYP/FallDetectionSystem/train3/weights/best.pt", confidence=0.5):
        """Load the YOLO model for fall detection."""
        self.model = YOLO(model_path)  
        self.confidence = confidence   

    def detect_fall(self, frame):
        """Process frame and detect falls using YOLO."""
        results = self.model(frame)
        for r in results:
            for box in r.boxes:
                if box.conf[0] > self.confidence and r.names[int(box.cls[0])] == "fall":
                    x1, y1, x2, y2 = map(int, box.xyxy[0])  # Get bounding box
                    return True, (x1, y1, x2, y2)  # Fall detected
        return False, None  # No fall detected
