import os
import shutil

# Prompt the user for the source directory
src = input("Enter the source directory path: ")
# Prompt the user for the destination directory
dst = input("Enter destination path: ")
# Set the path to the  source directory
path = src

# Check if the source directory exist
if not os.path.exists(src):
    print("Source directory doesn't exist")
    raise Exception("Source directory doesn't exists")

try:
    # Iterate over the list of the filenames in the src directory
    for file_name in os.listdir(path):
        if os.path.isfile(os.path.join(path, file_name)):  # Check if it's a file
            # Split the file to extract extension and convert to string
            file_extension = file_name.split('.')[-1]
            # Create the destination path based on the file extension
            path_dst = os.path.join(dst, file_extension)

            # Creates a directory if it doesn't exist yet
            if not os.path.exists(path_dst):
                os.mkdir(path_dst)

            # Provide the complete path of source path by combining the path and file_name
            source_path = os.path.join(path, file_name)
            # Provide the complete path of destination path by combining the path destination  and file_name
            destination_path = os.path.join(path_dst, file_name)
            # Move the source path to the destination path
            shutil.move(source_path, destination_path)

    print("Welp, that was fast! Categorizing of files is now completed.... ")
except Exception as e:
    print(f"An error occurred {e}")
