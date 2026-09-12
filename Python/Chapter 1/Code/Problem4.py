import os

# Specify the directory path (use '.' for current directory)
directory_path = '/Python'

try:
    # Get the list of files and directories
    contents = os.listdir(directory_path)
    
    print(f"Contents of directory '{directory_path}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print("The directory does not exist.")
except PermissionError:
    print("Permission denied to access the directory.")
