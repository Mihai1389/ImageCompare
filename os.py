import os

# Example 1: Working with directories
current_dir = os.getcwd()  # Get current working directory
print("Current directory:", current_dir)

# Example 2: Listing files in a directory
files = os.listdir(current_dir)
print("Files in current directory:", files)

# Example 3: Creating a directory
new_dir = os.path.join(current_dir, "new_directory")
os.makedirs(new_dir, exist_ok=True)  # Create new directory if it doesn't exist

# Example 4: Renaming a file
file_to_rename = os.path.join(current_dir, "old_file.txt")
new_name = os.path.join(current_dir, "new_file.txt")
os.rename(file_to_rename, new_name)

# Example 5: Environment variables
python_path = os.getenv('PYTHONPATH')
print("PYTHONPATH:", python_path)

