from ultralytics.utils.benchmarks import benchmark

# Benchmark on GPU
benchmark(model="D:/UNI/FYP/FallDetectionSystem/train/weights/best.pt", data="D:/UNI/FYP/FallDetectionSystem/Fall-Detection-CaucaFall-5/data.yaml", imgsz=640, half=False, device= 0)

# Benchmark specific export format
# benchmark(model="yolo11n.pt", data="coco8.yaml", imgsz=640, format="onnx")