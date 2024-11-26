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
    
def click_save_per_page(firstID, firstButtonLoc, nClicks, config):
    buttonInterval = config['buttonInterval']
    rightClick_x = config['rightClick_x']
    rightClick_y = config['rightClick_y']
    rel_saveAs_x = config['rel_saveAs_x']
    rel_saveAs_y = config['rel_saveAs_y']
    
    firstButtonX, firstButtonY = firstButtonLoc
    
    for i in range(nClicks):
        # 1. Move mouse and click the button
        # Each click can be executed by just passing coordinates directly into the function (e.g. click(xPos, yPos) )
        # but it is safer to see with your own eyes if the mouse is moving towards correct locations
        pyautogui.moveTo(firstButtonX, firstButtonY + buttonInterval*i)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.click()
        
        # pop-up page takes time to load. At least 3 seconds (Otherwise, it will click on the wrong page)
        time.sleep(3)
        
        # 2. Right click on blank white space of popped-up page
        pyautogui.moveTo(rightClick_x, rightClick_y)
        pyautogui.rightClick()
        time.sleep(0.5)
        
        # 3. Click 'Save As'
        pyautogui.moveRel(rel_saveAs_x, rel_saveAs_y)
        pyautogui.click()
        # Wait for 'Save As' dialog to appear
        time.sleep(1)
        
        # 4. Change the file name (file name is identical to column ID, which is integer)
        pyautogui.write(f"{firstID-i}")
        time.sleep(0.5)
        
        # 5. Press enter (same effect as clicking 'save' button)
        pyautogui.press('enter')
        
        # Wait for save operation to complete
        time.sleep(1)

    print(f"Completed {nClicks} save operations.")
    
    
if __name__ == "__main__":
    config = load_config()
    
    # The patient's ID in the top column (where first 'Review' button is located)
    # This will be used as the file name for the first file.
    # And then, the number will be decremented for each file.
    firstID = int(input("Enter the first ID number: "))

    nClicks = int(input("Enter the number of clicks: "))
    
    firstButtonX, firstButtonY = 0, 0
    start_time = time.time()
    
    while True:
        # Move mouse onto the first 'Review' button
        if keyboard.is_pressed('space'):
            firstButtonX, firstButtonY = pyautogui.position()
            # keyboard.wait('space', suppress=True)
            time.sleep(0.1) # Small delay to prevent rapid repeated executions
        # Any other hotkeys don't seem to work in Mac
        # elif keyboard.is_pressed('shift'):
        #     break    
        if time.time() - start_time > 5:
            break
    
    firstButtonLoc = (firstButtonX, firstButtonY)
    click_save_per_page(firstID, firstButtonLoc, nClicks, config)
    