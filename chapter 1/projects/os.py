import os

# Get the current working directory
directory_path = os.getcwd()

# List all files and directories in the current directory
try:
    contents = os.listdir(directory_path)
    print(f"Contents of directory '{directory_path}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print("The directory does not exist.")
except PermissionError:
    print("You do not have permission to access this directory.")
