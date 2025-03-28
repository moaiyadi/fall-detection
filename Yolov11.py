from ultralytics import YOLO

# Load a model
model = YOLO("yolo11n.yaml")  # build a new model from YAML
model = YOLO("yolo11n.pt")  # load a pretrained model (recommended for training)
model = YOLO("yolo11n.yaml").load("D:/UNI/FYP/FallDetectionSystem/yolo11n.pt")  # build from YAML and transfer weights

# Train the model
results = model.train(data="D:/UNI/FYP/FallDetectionSystem/Datasets/Roboflow/data.yaml", epochs=2, imgsz=640, device = 0, batch = 1 )

# from ultralytics import YOLO

# if __name__ == "__main__":
#     # Load a model
#     model = YOLO("D:/UNI/FYP/FallDetectionSystem/yolo11x.pt")  # load a partially trained model

#     # Resume training
#     results = model.train(resume=True, device = 'cpu')