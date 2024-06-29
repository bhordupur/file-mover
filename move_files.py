import os
import sys
import shutil

'''
usage:
    python move_files.py /path/to/source/folder /path/to/target/folder
'''

def move_specific_files(source_directory, target_directory):
    '''
    Need to find the files with certain pattern in a given directory
    Move the files to a new directory
    Create directory if that directory is not existed
    if no match is found then simply print a message
    '''

    # List all files in the specified directory
    files_in_directory = os.listdir(source_directory)
    
    # Define the patterns to look for
    # On phone file names IMG_5088 2.jpeg or IMG_5088 2.MOV or IMG_5088 (1).MOV
    patterns = [" 2.jpeg", " 2.MOV", " (1).MOV"]
    
    # Filter files that match any of the patterns
    files_to_move = [file for file in files_in_directory if any(file.endswith(pattern) for pattern in patterns)]
   
    if not files_to_move:
        print("No match found.")
        return
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)
    
    # Move each filtered file
    for file in files_to_move:
        source_file_path = os.path.join(source_directory, file)
        target_file_path = os.path.join(target_directory, file)
        try:
            shutil.move(source_file_path, target_file_path)
            print(f"Moved: {source_file_path} -> {target_file_path}")
        except Exception as e:
            print(f"Error moving {source_file_path} to {target_file_path}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python move_files.py <source_directory> <target_directory>")
        sys.exit(1)

    # Get the source and target directories from the command-line arguments
    source_directory = sys.argv[1]
    target_directory = sys.argv[2]

    if not os.path.isdir(source_directory):
        print(f"The specified source directory does not exist: {source_directory}")
        sys.exit(1)

    move_specific_files(source_directory, target_directory)

