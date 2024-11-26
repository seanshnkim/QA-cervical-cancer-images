import pyautogui
import keyboard

'''
CAUTIONS:
You MUST run this code with administrator privilege.
e.g. `sudo python3 find_pixel_pos.py`
'''

def print_mouse_position():
    x, y = pyautogui.position()
    print(f"Mouse position: X: {x}, Y: {y}")

print("Press 'space' to print mouse position. Press 'ctrl+shift+space' to quit.")

while True:
    if keyboard.is_pressed('space'):
        print_mouse_position()
        keyboard.wait('space')
    # This doesn't seem to work in Mac
    elif keyboard.is_pressed('ctrl+shift+esc'):
        break
print("Program ended.")