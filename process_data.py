import os
import json

def process_folders(saved_dir, start_idx, end_idx):
    omitted_folders = []

    # Step 2: Iterate through folders and check for jpg files
    for i in range(start_idx, end_idx + 1):
        folder_name = f'{i}_files'
        folder_path = os.path.join(saved_dir, folder_name)

        if not os.path.isdir(folder_path):
            omitted_folders.append(folder_name)
            continue

        jpg_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg')]
        if not jpg_files:
            omitted_folders.append(folder_name)

    # Step 3: Process folders if no omissions
    if len(omitted_folders) == 0:
        # Step 3-1: Remove HTML files
        for file in os.listdir(saved_dir):
            if file.endswith('.html'):
                os.remove(os.path.join(saved_dir, file))

        # Steps 3-2 to 3-4: Process each folder
        for i in range(start_idx, end_idx + 1):
            folder_name = f'{i}_files'
            folder_path = os.path.join(saved_dir, folder_name)
            jpg_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg')]

            # Rename jpg files
            for idx, jpg_file in enumerate(jpg_files, start=1):
                new_name = f'{i}_{idx}.jpg'
                os.rename(os.path.join(folder_path, jpg_file), os.path.join(folder_path, new_name))

            # Remove non-jpg files
            for file in os.listdir(folder_path):
                if not file.endswith('.jpg'):
                    os.remove(os.path.join(folder_path, file))

    # Dump omitted_folders to a JSON file
    json_file_path = os.path.join(saved_dir, 'omitted_folders.json')
    with open(json_file_path, 'w') as json_file:
        json.dump({"omitted_folders": omitted_folders}, json_file, indent=4)
        
    return len(omitted_folders)

# Example usage
saved_dir = 'data'
start_idx = 1
end_idx = 171
nOmitted = process_folders(saved_dir, start_idx, end_idx)

print("The number of omitted folders:", nOmitted)