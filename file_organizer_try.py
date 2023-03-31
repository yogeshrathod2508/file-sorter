import os,sys,subprocess
from tabulate import tabulate
from data import *
import shutil
# region Getting file details and storing them in a list
def get_file_details(selected_directory):
    file_details = []
    for root, dirs, files in os.walk(selected_directory):
        for filename in files:
            # Get the file path
            file_path = os.path.join(root, filename)

            # Get the extension of the file
            file_extension = os.path.splitext(file_path)[1]
            
            file_details.append({'file_name':filename, 'file_path': file_path,'file_extension': file_extension})
    return file_details
# endregion

# region Grouping Files according to extensions
def group_files(file_details):
    grouped_files = {}  
    for file_ob in file_details:
        if file_ob['file_extension'] in grouped_files:
            grouped_files[file_ob['file_extension']].append(file_ob)
        else:
            grouped_files[file_ob['file_extension']] = [file_ob]
    return grouped_files
# endregion


selected_directory = ''
if len(sys.argv) > 1:
    selected_directory = sys.argv[1:][0]
    file_details = get_file_details(selected_directory)
    grouped_files = group_files(file_details)
    
    # region Moving Files according to extensions to their corresponding folders
    def move_files(grouped_files):
        for extension,files in grouped_files.items():
            directory_name = extension.split(".")[1]  ## we will make directory having extension as it's name
            for file_ob in files:
                new_directory_path = os.path.join(os.path.dirname(file_ob['file_path']), directory_name)
                if not os.path.exists(new_directory_path):
                    os.makedirs(new_directory_path)  #creating directory if not exists
                new_file_path = os.path.join(os.path.dirname(file_ob['file_path']), directory_name)
                try:
                    shutil.move(file_ob['file_path'],new_file_path)
                except:
                    print('Error moving file')
    # endregion
    move_files(grouped_files)

else:
    print("No folder selected")
 

asd = input('✅ Done Moving Files.\nPress ENTER to exit')