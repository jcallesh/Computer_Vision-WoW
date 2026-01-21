"""
===============================================================================
 Name        : map_reader.py
 Author(s)   :
 Version     : 0.1
 Description :  Extracts zone information from map screenshots using OCR.
            
 notes:
    -  Requires Tesseract OCR installed and configured.

===============================================================================

 

"""

import pyautogui
import pytesseract as pytesseract
import numpy as np
import cv2 as cv

# Path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = (
    r'C:\Users\juanm\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
)

def get_current_zone(img):
    """
    Extract and return the current zone name from a given image.
    
    Args:
        img (numpy.ndarray): Screenshot image array.
    
    Returns:
        str: Detected zone name text.
    """
    top_left_zone = (1655, 34)
    bottom_right_zone = (1974, 69)

    # Crop region containing zone name
    img_zone_name = img[
        top_left_zone[1]:bottom_right_zone[1],
        top_left_zone[0]:bottom_right_zone[0]
    ]

    # OCR text recognition from images
    zone_name = pytesseract.image_to_string(img_zone_name)

    return zone_name
