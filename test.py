"""
===============================================================================
 Name        : test.py
 Author(s)   :
 Version     : 0.1
 Description : Test script for YOLO inference on a screenshot image.

 notes:
    -  Requires Ultralytics YOLO and OpenCV.

===============================================================================

 

"""

import cv2 as cv
from ultralytics import YOLO
import numpy as np

# Load and resize image
img = cv.imread(r'files\Screenshot 2025-01-15 223726.png')
small_img = cv.resize(img, (640, 640))

# Display original resized image
cv.imshow('Computer Vision', small_img)
cv.waitKey(10000)

# Load YOLO model and run inference
model = YOLO(r"runs\detect\train3\weights\best.onnx")
results = model(small_img, device='cpu')

# Annotated image with detections
annotated_img = results[0].plot()

# Optional: Access bounding boxes, confidences, and labels
# boxes = results[0].boxes.xyxy.numpy()
# confidences = results[0].boxes.conf.numpy()
# labels = results[0].boxes.cls.numpy()
# for box, conf, label in zip(boxes, confidences, labels):
#     x1, y1, x2, y2 = map(int, box)
#     label = int(label)
#     cv.rectangle(annotated_img, (x1, y1), (x2, y2), (255, 0, 0), 2)
#     cv.putText(annotated_img, f"{label} {conf:.2f}", (x1, y1-10),
#                cv.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

# Display detection results
cv.imshow("Detection Result", annotated_img)
cv.waitKey(0)
cv.destroyAllWindows()
