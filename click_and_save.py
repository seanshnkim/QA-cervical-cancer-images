import pyautogui
import keyboard
import time
import json


'''
CAUTIONS:
1. This code automatically moves mouse on screen.
It is set to MacBook Air M1 12.9 inch screen, Chrome web browser, zoom 50% 
Because the pixel values are hard-coded, it may result in different outputs for each individual.

2. Before running the code, go to Chrome Webrowser where the target webpage is open. 
Settings > Downloads, and disable 'Show downloads when they're done'

3. Make sure as soon as you start the code, 
the target window should be active in less than 5 seconds.

4. In the directory (for me, the default directory is ~/Downloads),
there should be no duplicated files.
'''

def load_config():
    with open('config.json', 'r') as config_file:
        return json.load(config_file)
    
def click_save_per_page(config, firstButtonX, firstButtonY):
    buttonInterval = config['buttonInterval']
    nButtons = config['nButtons']
    rightClick_x = config['rightClick_x']
    rightClick_y = config['rightClick_y']
    rel_saveAs_x = config['rel_saveAs_x']
    rel_saveAs_y = config['rel_saveAs_y']
    patientID = config['patientID']
    
    for i in range(nButtons):
        # 1. Move mouse and click the button
        # Each click can be executed by just passing coordinates directly into the function (e.g. click(xPos, yPos) )
        # but it is safer to see with your own eyes if the mouse is moving towards correct locations
        pyautogui.moveTo(firstButtonX, firstButtonY + buttonInterval*i)
        pyautogui.click()
        time.sleep(1)
        
        # 2. Right click on blank white space of popped-up page
        pyautogui.moveTo(rightClick_x, rightClick_y)
        pyautogui.rightClick()
        time.sleep(0.2)
        
        # 3. Click 'Save As'
        pyautogui.moveRel(rel_saveAs_x, rel_saveAs_y)
        pyautogui.click()
        # Wait for 'Save As' dialog to appear
        time.sleep(1)
        
        # 4. Change the file name (file name is identical to column ID, which is integer)
        pyautogui.write(f"{patientID-i}")
        time.sleep(0.5)
        
        # 5. Press enter (same effect as clicking 'save' button)
        pyautogui.press('enter')
        
        # Wait for save operation to complete
        time.sleep(1)

    print(f"Completed {nButtons} save operations.")
    
    
if __name__ == "__main__":
    config = load_config()
    
    # Wait for enough time to switch to the target window
    # time.sleep(5)
    
    # Move mouse onto the first 'Review' button
    
    firstButtonX, firstButtonY = 0, 0
    
    while True:
        if keyboard.is_pressed('space'):
            firstButtonX, firstButtonY = pyautogui.position()
            keyboard.wait('space', suppress=True)
        # Any other hotkeys don't seem to work in Mac
        elif keyboard.is_pressed('shift'):
            break    
    click_save_per_page(config, firstButtonX, firstButtonY)
    