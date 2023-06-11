import os
import shutil
import pyautogui
import time

#TO-DO: falta agregar que detecte cuando envien una imagen nueva

def download_imgs():
    # Delay between each action (adjust as needed)
    delay = 1

    # Press Windows key to open the Start menu
    pyautogui.press('win')

    # Wait for the Start menu to open
    time.sleep(delay)

    # Type 'chrome' and press Enter to open Chrome
    pyautogui.typewrite('chrome')
    pyautogui.press('enter')

    # Wait for Chrome to open
    time.sleep(delay)

    # Maximize the Chrome window (optional)
    pyautogui.hotkey('win', 'up')

    # Wait for Chrome to maximize
    time.sleep(delay)

    # Navigate to WhatsApp Web
    pyautogui.typewrite('web.whatsapp.com')
    pyautogui.press('enter')

    # Wait for WhatsApp Web to load
    time.sleep(8)

    pre_image_location = pyautogui.locateCenterOnScreen("./clicklist/pre.png", confidence=0.8)
    pyautogui.click(pre_image_location)

    time.sleep(5)
    
    # Press SHIFT+CTRL+J to open the JavaScript console
    pyautogui.hotkey('shift', 'ctrl', 'j')

    # Wait for the JavaScript console to open
    time.sleep(2)

    # Click on the pre.png image
    pre_image_location = pyautogui.locateCenterOnScreen("./clicklist/pre2.png", confidence=0.8)
    pyautogui.click(pre_image_location)

    time.sleep(1)
    # Read the JavaScript code from the file
    with open('download_imgs.js', 'r') as file:
        javascript_code = file.read()

    # Execute the JavaScript code in the console
    pyautogui.typewrite(javascript_code)
    time.sleep(1)
    pyautogui.press('enter')

    # Wait for the code to execute
    time.sleep(5)

def move_imgs():
    downloads_folder = r"C:\Users\SgO\Downloads"  # Replace with the path to your downloads folder
    destination_folder = r"./imgs"  # Replace with the correct destination folder path

    # Get a list of files in the downloads folder
    files = os.listdir(downloads_folder)

    # Iterate over the files in the downloads folder
    for file in files:
        if file.startswith("automatic_whatsap_image_scraper_") and file.endswith(".jpg"):
            print('test')
            # Create the destination path
            destination = os.path.join(destination_folder, file)

            # Move the file to the destination folder
            shutil.move(os.path.join(downloads_folder, file), destination)
            print(f"Moved {file} to {destination}")

    # Borrar todos menos la ultima imagen enviada

    directory = "./imgs"  # Replace with the correct destination folder path

    # Get a list of image files in the directory with the ".jpg" extension
    image_files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f.endswith(".jpg")]

    # Sort the image files in descending order
    image_files.sort(reverse=True)

    # Keep the last image file (highest number)
    image_files_to_keep = image_files[:1]
    print(image_files_to_keep)

    # Iterate over the image files and delete the ones to be removed
    for image_file in image_files:
        if image_file not in image_files_to_keep:
            file_path = os.path.join(directory, image_file)
            os.remove(file_path)
            print(f"Deleted {image_file}")
    
    return image_files_to_keep[0]

def create_and_send_sticker(filename):
    # Wait for a few seconds before starting the automation
    time.sleep(3)

    # Press the Windows key to open the start menu
    pyautogui.press("win")

    # Type and open Chrome
    pyautogui.write("chrome")
    pyautogui.press("enter")

    # Wait for a few seconds for Chrome to open
    time.sleep(5)

    # Open WhatsApp Web
    pyautogui.write("web.whatsapp.com")
    pyautogui.press("enter")

    # Wait for a few seconds for WhatsApp Web to load
    time.sleep(10)

    # Click on the pre.png image
    pre_image_location = pyautogui.locateCenterOnScreen("./clicklist/pre.png", confidence=0.8)
    pyautogui.click(pre_image_location)

    # Wait for a few seconds
    time.sleep(2)

    # Click on the 1.png image
    image_1_location = pyautogui.locateCenterOnScreen("./clicklist/1.png", confidence=0.8)
    pyautogui.click(image_1_location)

    # Wait for a few seconds
    time.sleep(2)

    # Click on the 2.png image
    image_2_location = pyautogui.locateCenterOnScreen("./clicklist/2.png", confidence=0.8)
    pyautogui.click(image_2_location)

    # Wait for a few seconds
    time.sleep(2)

    # Click on the 3.png image
    image_3_location = pyautogui.locateCenterOnScreen("./clicklist/3.png", confidence=0.8)
    pyautogui.click(image_3_location)

    # Wait for a few seconds
    time.sleep(2)

    # Enter the last image's full filename and press enter
    last_image_filename = str(filename)
    pyautogui.write(last_image_filename)
    pyautogui.press("enter")

    # Wait for a few seconds
    time.sleep(2)

    # Click on the 4.png image
    image_4_location = pyautogui.locateCenterOnScreen("./clicklist/4.png", confidence=0.8)
    pyautogui.click(image_4_location)

if __name__ == "__main__":
    download_imgs()
    filename = move_imgs()
    create_and_send_sticker(filename)