import json

# This is set to MacBook Air M1 12.9 inch screen, Chrome web browser, zoom 50%
config = {
    # Pixel position of first button
    "xPos": 1157,
    "yPos": 250,
    
    # Pixel size (vertically) between each button
    "ySize": 23.6,
    
    # The number of 'Review' button in current page
    "nButtons": 23,
    
    # Pixel position of 'save as' button relative to the right-clicked button
    "rightClick_x": 834,
    "rightClick_y": 172,
    
    # Relative (not absolute!!) pixel position for 'save as'
    "rel_saveAs_x": 51,
    "rel_saveAs_y": 88,
    
    # The patient's ID in the top column (where first 'Review' button is located)
    # This will be used as the file name for the first file.
    # And then, the number will be incremented for each file.
    "patientID": 67
}

# Save the configuration to a config.json file
with open('config.json', 'w') as config_file:
    json.dump(config, config_file, indent=4)