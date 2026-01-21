"""
===============================================================================
 Name        : yolo_train.py
 Author(s)   :
 Version     : 0.1
 Description : Train and export YOLO model for object detection.
            
 notes:
    -  Requires Ultralytics YOLO package and dataset YAML file.
===============================================================================

 

"""

from multiprocessing import freeze_support
from ultralytics import YOLO


def main():
    """
    Train YOLO model, validate results, and export to ONNX format.
    """
    # Load YOLO model
    model = YOLO("yolo11n.pt")

    # Train model
    train_results = model.train(
        data=r"WoW Wolves.v2i.yolov11\data.yaml",  # dataset YAML path
        epochs=100,                                # training epochs
        imgsz=640,                                 # image size
        device='cuda',                             # training device
    )

    # Validate model
    metrics = model.val()

    # Export model to ONNX
    model.to('cpu')
    success = model.export(format="onnx")

    print("Training completed, evaluation finished, and model exported to ONNX.")


if __name__ == '__main__':
    freeze_support()  # Required if script is frozen into an executable
    main()
