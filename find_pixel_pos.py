import pyautogui
import keyboard
import time

'''
CAUTIONS:
You MUST run this code with administrator privilege.
e.g. `sudo python3 find_pixel_pos.py`
'''

def print_mouse_position():
    x, y = pyautogui.position()
    print(f"Mouse position: X: {x}, Y: {y}")

print("Press 'space' to print mouse position. Press 'end' to quit.")

while True:
    if keyboard.is_pressed('space'):
        # keyboard.wait('space', suppress=True)
        print_mouse_position()
        time.sleep(0.1)  # Small delay to prevent rapid repeated executions
    # Any other hotkeys don't seem to work in Mac
    elif keyboard.is_pressed('shift'):
        # keyboard.release('space')
        break
print("Program ended.")