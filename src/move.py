"""
===============================================================================
 Name        : move.py
 Author(s)   :
 Version     : 0.1
 Description : Provides movement control functions using keyboard automation.
            
 notes:
    -  Requires pyautogui library.
===============================================================================

 

"""

import pyautogui
import time

# Key bindings
KEY_RUN = None
KEY_JUMP = 'space'
KEY_MOVE_UP = 'w'
KEY_MOVE_DOWN = 's'
KEY_MOVE_LEFT = 'a'
KEY_MOVE_RIGHT = 'd'
KEY_STRAFE_LEFT = 'q'
KEY_STRAFE_RIGHT = 'e'
KEY_SHEATHE = 'z'
KEY_SIT = 'x'


def forward_start():
    """Hold forward movement key."""
    pyautogui.keyDown(KEY_MOVE_UP)

def forward_stop():
    """Release forward movement key."""
    pyautogui.keyUp(KEY_MOVE_UP)


def backward_start():
    """Hold backward movement key."""
    pyautogui.keyDown(KEY_MOVE_DOWN)

def backward_stop():
    """Release backward movement key."""
    pyautogui.keyUp(KEY_MOVE_DOWN)


def left_start():
    """Hold left movement key."""
    pyautogui.keyDown(KEY_MOVE_LEFT)

def left_stop():
    """Release left movement key."""
    pyautogui.keyUp(KEY_MOVE_LEFT)


def right_start():
    """Hold right movement key."""
    pyautogui.keyDown(KEY_MOVE_RIGHT)

def right_stop():
    """Release right movement key."""
    pyautogui.keyUp(KEY_MOVE_RIGHT)


def strafe_left_start():
    """Hold strafe left key."""
    pyautogui.keyDown(KEY_STRAFE_LEFT)

def strafe_left_stop():
    """Release strafe left key."""
    pyautogui.keyUp(KEY_STRAFE_LEFT)


def strafe_right_start():
    """Hold strafe right key."""
    pyautogui.keyDown(KEY_STRAFE_RIGHT)

def strafe_right_stop():
    """Release strafe right key."""
    pyautogui.keyUp(KEY_STRAFE_RIGHT)


def jump():
    """Press jump key once."""
    pyautogui.press(KEY_JUMP)

def sit():
    """Press sit key once."""
    pyautogui.press(KEY_SIT)


def bump_forward(deltatime=0.05):
    """Tap forward key for a short duration."""
    forward_start()
    time.sleep(deltatime)
    forward_stop()

def bump_backward(deltatime=0.05):
    """Tap backward key for a short duration."""
    backward_start()
    time.sleep(deltatime)
    backward_stop()

def bump_left(deltatime=0.05):
    """Tap left key for a short duration."""
    left_start()
    time.sleep(deltatime)
    left_stop()

def bump_right(deltatime=0.05):
    """Tap right key for a short duration."""
    right_start()
    time.sleep(deltatime)
    right_stop()


if __name__ == '__main__':
    time.sleep(10)
    print('Testing movement functions')
    print('Forward')
    bump_forward(10)
    print('Backward')
    bump_backward(5)
    print('Left')
    bump_left(3)
    print('Right')
    bump_right(8)
    print('Done :)')
