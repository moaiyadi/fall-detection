# from roboflow import Roboflow
# rf = Roboflow(api_key="KvsGUXdoY9TgVZjYJtx2")
# project = rf.workspace("falldetection-bwfdz").project("fall-detection-caucafall")
# version = project.version(1)
# dataset = version.download("yolov11")



# from roboflow import Roboflow
# rf = Roboflow(api_key="KvsGUXdoY9TgVZjYJtx2")
# project = rf.workspace("falldetection-bwfdz").project("fall-detection-caucafall")
# version = project.version(5)
# dataset = version.download("yolov11")




# from roboflow import Roboflow
# rf = Roboflow(api_key="KvsGUXdoY9TgVZjYJtx2")
# project = rf.workspace("falldetection-bwfdz").project("fall-detection-ehgga")
# version = project.version(1)
# dataset = version.download("yolov11")



from roboflow import Roboflow
rf = Roboflow(api_key="KvsGUXdoY9TgVZjYJtx2")
project = rf.workspace("falldetection-bwfdz").project("yolo-dataset-98swd")
version = project.version(2)
dataset = version.download("yolov11")
                
                           