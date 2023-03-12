import os

# Create a folder on desktop
folder_name = "screenshots"
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
folder_path = os.path.join(desktop_path, folder_name)
os.makedirs(folder_path, exist_ok=True)

# Save screenshot in the folder
file_name = "screenshot.png"
file_path = os.path.join(folder_path, file_name)
driver.save_screenshot(file_path)
