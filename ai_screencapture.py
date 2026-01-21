"""
===============================================================================
 Name        : ai_screencapture.py
 Author(s)   :
 Version     : 0.1
 Description : Screen capture agent with health/mana detection and YOLO inference.

 notes:
    -  Requires mss, pyautogui, OpenCV, numpy, torch, and Ultralytics YOLO.

===============================================================================

 

"""

import mss
import pyautogui
import cv2 as cv
import numpy as np
import time
import multiprocessing
import torch

# Custom imports
import src.utils as utils
import src.spells as spells
import src.map_reader as map_reader

# Display Configurations
SHOW_COMP_VISION_WINDOW = True
SHOW_HEALTH_BAR_WINDOW = True
SHOW_MANA_BAR_WINDOW = True

# Screen scaling
old_width, old_height = 1920, 1080
new_width, new_height = 1920, 1080  # or 640, 640
scale_x = new_width / old_width
scale_y = new_height / old_height


def hue_match_pct(img, hue, hue_tolerance=10, bar='health'):
    """
    Calculate percentage of pixels matching a hue range.

    Args:
        img (numpy.ndarray): Image region to analyze.
        hue (int): Target hue value.
        hue_tolerance (int): Allowed deviation from target hue.
        bar (str): 'health' or 'mana' for potion casting.

    Returns:
        float: Percentage of matching pixels.
    """
    hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    ratio = 360 / 180
    lower_bound = ((hue - hue_tolerance) / ratio) % 180
    upper_bound = ((hue + hue_tolerance) / ratio) % 180

    mask = (hsv_img[:, :, 0] >= lower_bound) & (hsv_img[:, :, 0] <= upper_bound) \
        if lower_bound < upper_bound else \
        (hsv_img[:, :, 0] >= lower_bound) | (hsv_img[:, :, 0] <= upper_bound)

    match_count = np.count_nonzero(mask)
    percet_pixels = match_count / hsv_img[:, :, 0].size * 100

    if percet_pixels <= 60 and (spells.can_cast_spell[f'{bar}_pot'] - time.time()) < 0:
        spells.cast_spell(f'{bar}_pot', 40)

    return percet_pixels


def rescale_coordinates(roi):
    """
    Rescale coordinates from 1920x1080 to new resolution.

    Args:
        roi (tuple[int, int, int, int]): Original coordinates (x1, y1, x2, y2).

    Returns:
        tuple[int, int, int, int]: Rescaled coordinates.
    """
    x1, y1, x2, y2 = roi
    return (
        int(x1 * scale_x),
        int(y1 * scale_y),
        int(x2 * scale_x),
        int(y2 * scale_y),
    )


class ScreenCaptureAgent:
    """
    Screen capture agent for health/mana detection and YOLO inference.
    """

    def __init__(self, model):
        self.img = None
        self.fps = None
        self.width, self.height = pyautogui.size()
        self.monitor = {"top": 0, "left": 0, "width": self.width, "height": self.height}

        # Predefined ROIs
        self.health_roi = rescale_coordinates((705, 804, 849, 809))
        self.mana_roi = rescale_coordinates((705, 819, 849, 823))

        self.model = model

    def capture_screen(self):
        """
        Continuously capture screen, analyze health/mana bars, and run YOLO inference.
        """
        fps_timer = time.time()
        fps_report_interval = 5.0
        frame_count = 0

        with mss.mss() as sct:
            while True:
                start_time = time.time()

                # Screen capture
                screen = sct.grab(self.monitor)
                img = np.array(screen)[:, :, :3]

                # ROI analysis
                img_health = img[self.health_roi[1]:self.health_roi[3], self.health_roi[0]:self.health_roi[2]]
                img_mana = img[self.mana_roi[1]:self.mana_roi[3], self.mana_roi[0]:self.mana_roi[2]]

                # Hue matching
                health_pct = hue_match_pct(img_health, 120, 20, 'health')
                mana_pct = hue_match_pct(img_mana, 240, 30, 'mana')

                # YOLO inference
                small_img = cv.resize(img, (640, 640))
                results = self.model(small_img, device='cpu', verbose=False)

                if SHOW_COMP_VISION_WINDOW:
                    small_img = results[0].plot()
                    cv.putText(small_img, f"FPS: {self.fps:.2f}" if self.fps else "FPS: ...",
                               (25, 50), cv.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 2, cv.LINE_AA)
                    cv.putText(small_img, f"Health: {health_pct:.2f}",
                               (25, 100), cv.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)
                    cv.putText(small_img, f"Mana: {mana_pct:.2f}",
                               (25, 150), cv.FONT_HERSHEY_DUPLEX, 1, (255, 0, 0), 2, cv.LINE_AA)

                    cv.imshow('Computer Vision', small_img)
                    cv.waitKey(1)

                # FPS calculation
                frame_count += 1
                if time.time() - fps_timer > fps_report_interval:
                    self.fps = frame_count / fps_report_interval
                    frame_count = 0
                    fps_timer = time.time()

                # Frame rate control
                elapsed = time.time() - start_time
                if elapsed < 1 / 60:
                    time.sleep(1 / 60 - elapsed)


def print_menu():
    """Print command menu for screen capture agent."""
    print("\n================= AI Screen Capture =================")
    print("\tr - run\t\tStart capturing screen")
    print("\ts - stop\tStop capturing screen")
    print("\tq - quit\tExit program")


if __name__ == '__main__':
    from ultralytics import YOLO

    model = YOLO(r"runs\detect\train\weights\best.onnx")
    screen_agent = ScreenCaptureAgent(model)
    capture_process = None

    while True:
        print_menu()
        user_input = input("Enter command: ").strip().lower()

        if user_input == 'q':
            if capture_process:
                capture_process.terminate()
            break

        if user_input == 'r' and not capture_process:
            capture_process = multiprocessing.Process(target=screen_agent.capture_screen)
            capture_process.start()

        elif user_input == 's' and capture_process:
            capture_process.terminate()
            capture_process = None
