import pyautogui
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
    
if __name__ == "__main__":
    config = load_config()
    
    xPos = config['xPos']
    yPos = config['yPos']
    ySize = config['ySize']
    nButtons = config['nButtons']
    rightClick_x = config['rightClick_x']
    rightClick_y = config['rightClick_y']
    rel_saveAs_x = config['rel_saveAs_x']
    rel_saveAs_y = config['rel_saveAs_y']
    patientID = config['patientID']
    
    # Wait for enough time to switch to the target window
    time.sleep(5)
    
    for i in range(nButtons):
        # 1. Move mouse and click the button
        # It can be achieved by just click(xPos, yPos), 
        # but it is safer to see with your own eyes if the mouse is on correct spot
        pyautogui.moveTo(xPos, yPos+ySize*i)
        pyautogui.click()
        time.sleep(1)
        
        # 2. Right click
        pyautogui.moveTo(rightClick_x, rightClick_y)
        pyautogui.rightClick()
        time.sleep(0.2)
        
        # 3. Click 'Save As'
        pyautogui.moveRel(rel_saveAs_x, rel_saveAs_y)
        pyautogui.click()
        # Wait for 'Save As' dialog to appear
        time.sleep(1)
        
        # 4. Change file name
        pyautogui.write(f"{patientID-i}")
        time.sleep(0.5)
        
        # 7. Click 'Save'
        pyautogui.press('enter')
        
        # Wait for save operation to complete
        time.sleep(1)

    print(f"Completed {nButtons} save operations.")