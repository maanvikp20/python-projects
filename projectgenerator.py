import os

# Get user inputs
projname = input("> What is the name of the project? \n")
authorname = input("> Who is the author? \n")

# Define main folder name and path
main_folder_name = projname
main_folder_path = os.path.abspath(main_folder_name)

# Create the main folder
os.mkdir(main_folder_name)
print(f"> Created main directory {main_folder_path}")

# Define subfolder name and path within the main folder
subfolder_name = 'src'
subfolder_path = os.path.join(main_folder_path, subfolder_name)

# Create the subfolder
os.mkdir(subfolder_path)
print(f"> Created subdirectory {subfolder_path}")

# List of file names to create in the main folder
outfilenames = ['README.md', 'TODO.md']

# Create each file in the main folder
for file in outfilenames:
    new_file_path = os.path.join(main_folder_path, file)
    with open(new_file_path, 'w') as f:
        if file == 'README.md':
            f.write(f"Project: {projname}\nAuthor: {authorname}\n")
    print(f"> Created file {new_file_path}")

# List of file names to create in the subfolder
srcfilenames = ['main.py']

# Create each file in the subfolder
for file in srcfilenames:
    src_file_path = os.path.join(subfolder_path, file)
    with open(src_file_path, 'w') as f:
        pass  # Create an empty file or add content as needed
    print(f"> Created file {src_file_path}")