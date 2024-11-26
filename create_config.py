import json

# This is set to MacBook Air M1 12.9 inch screen, Chrome web browser, zoom 50%
config = {
    # Pixel size (vertically) between each button
    "buttonInterval": 23.6,
    
    # Pixel position of 'save as' button relative to the right-clicked button
    "rightClick_x": 834,
    "rightClick_y": 172,
    
    # Relative (not absolute!!) pixel position for 'save as'
    "rel_saveAs_x": 51,
    "rel_saveAs_y": 88,
}

# Save the configuration to a config.json file
with open('config.json', 'w') as config_file:
    json.dump(config, config_file, indent=4)