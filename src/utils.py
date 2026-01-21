"""
===============================================================================
 Name        : utils.py
 Author(s)   :
 Version     : 0.1
 Description : Utility functions for capturing screen coordinates.
            
 notes:
    -  Requires pyautogui library.
===============================================================================

 

"""

import pyautogui


def get_cursor_positions():
    """
    Record mouse positions for defined points.

    Prompts the user to move the cursor to specific screen points
    and returns their coordinates.

    Returns:
        list[tuple[int, int]]: List of recorded (x, y) positions.
    """
    cursor_positions = []
    point_descriptions = [
        "Top-Left point",
        "Bottom-Right point",
    ]

    print("Move your mouse to each point when prompted and press Enter.")
    print("---------------------------------------------------------")

    for i, description in enumerate(point_descriptions):
        input(f"Move your cursor to the '{description}' and press Enter...")
        x, y = pyautogui.position()
        cursor_positions.append((x, y))
        print(f"Point {i+1} ({description}) recorded at: ({x}, {y})\n")

    print("All points recorded successfully!")
    return cursor_positions


if __name__ == '__main__':
    positions = get_cursor_positions()

    for i, pos in enumerate(positions):
        print(f"Point {i+1}: {pos}")

    print("Done :)")
