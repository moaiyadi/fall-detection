# from ultralytics import YOLO

# if __name__ == "__main__":
#     # Load a model
#     model = YOLO("yolo11m.pt")  # load an official model
#     model = YOLO("D:./UNI/FYP/FallDetectionSystem/runs(Latest)/detect/train/weights/best.pt")  # load a custom model

#     # Validate the model
#     metrics = model.val(data = "D:/UNI/FYP/FallDetectionSystem/Fall-Detection-1/data.yaml")  # no arguments needed, dataset and settings remembered
#     metrics.box.map  # map50-95
#     metrics.box.map50  # map50
#     metrics.box.map75  # map75
#     metrics.box.maps  # a list contains map50-95 of each category

from ultralytics import YOLO

# Load a model
model = YOLO("D:/UNI/FYP/FallDetectionSystem/runs/detect/train/weights/best.pt")

# Customize validation settings
validation_results = model.val(data="D:/UNI/FYP/FallDetectionSystem/Fall-Detection-1/data.yaml", imgsz=640, batch=16, conf=0.75, iou=0.6, device="cpu")