import os
import shutil

def move_imgs():
    downloads_folder = r"C:\Users\SgO\Downloads"  # Replace with the path to your downloads folder
    destination_folder = "./"

    # Get a list of files in the downloads folder
    files = os.listdir(downloads_folder)

    # Iterate over the files in the downloads folder
    for file in files:
        if file.startswith("automatic_whatsap_image_scraper_") and file.endswith(".jpeg"):
            # Create the destination path
            destination = os.path.join(destination_folder, file)

            # Move the file to the destination folder
            shutil.move(os.path.join(downloads_folder, file), destination)
            print(f"Moved {file} to {destination}")

    # Borrar todos menos la ultima imagen enviada

    directory = "./"

    # Get a list of image files in the directory with the ".jpeg" extension
    image_files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f.endswith(".jpeg")]

    # Sort the image files in descending order
    image_files.sort(reverse=True)

    # Keep the last image file (highest number)
    image_files_to_keep = image_files[:1]

    # Iterate over the image files and delete the ones to be removed
    for image_file in image_files:
        if image_file not in image_files_to_keep:
            file_path = os.path.join(directory, image_file)
            os.remove(file_path)
            print(f"Deleted {image_file}")

move_imgs()
