# Computer_Vision-WoW

This repository contains a simple implementation of a computer vision project to detect objects in a game.

---

## 🚀 Objective
- Train a YOLOv11 model for object detection in real-time video recording
- Apply detection to gameplay scenarios for automated responses (movement, spells, etc.)

---

## 📂 Project Structure

- **src/map_reader.py** -> Extracts zone names from screenshots using OCR  
- **src/move.py** -> Automates movement controls with `pyautogui`  
- **src/spells.py** -> Handles spell casting with cooldown tracking  
- **src/utils.py** -> Utility functions for screen coordinate capture
- **src/train_yolo.py** -> Training script for YOLOv11 model  
- **ai_screencapture.py** -> Main screen capture agent with health/mana detection and YOLO inference  
- **test.py** -> Test script for running inference on sample images  

Training dataset is provided here: [WoW Wolves Dataset](https://universe.roboflow.com/frank-pereny-dan82/wow-wolves/dataset/2)

---

📝 Notes
- Ensure Tesseract OCR is installed and properly configured if using OCR features
- GPU acceleration is recommended for YOLO training and inference
- Scripts are modular and can be adapted for other object detection tasks
- This implementation is based on [yolo-opencv-detector](https://github.com/moises-dias/yolo-opencv-detector),[opencv_tutorials](https://github.com/learncodebygaming/opencv_tutorials) and [AI Gaming Health Bar Monitor](https://github.com/fjpereny/youtube_tutorials)

---
## 🤝 Contributing
Contributions, suggestions, and improvements are welcome!
Feel free to open an issue or submit a pull request.

