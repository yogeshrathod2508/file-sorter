import os,sys,subprocess
from tabulate import tabulate
import shutil

if len(sys.argv) > 1:
    selected_directory = sys.argv[1:][0]
    directory_contents = os.listdir(selected_directory)
    
    file_details = []
    

    # region Getting file details and storing them in a list
    for file in directory_contents :
        # Get the file path
        file_path = os.path.join(selected_directory, file)

        # Get the file size in bytes
        file_size = os.path.getsize(file_path)

        # Get the extension of the file
        file_extension = os.path.splitext(file_path)[1]
        
        # Get the file creation time
        created_time = os.path.getctime(file_path)

        # Get the file modification time
        modified_time = os.path.getmtime(file_path)

        file_details.append({'file':file, 'file_path': file_path,'file_extension': file_extension , 'file_size':file_size, 'created_time': created_time, 'modified_time': modified_time})
    # endregion

    # print(tabulate(file_details, headers=['File name', 'File Path','File size', 'Created time', 'Modified time'], tablefmt='orgtbl'))
    # print(file_details)

    # region Grouping Files according to extensions
    grouped_files = {}  
    for dt in file_details:
        if dt['file_extension'] in grouped_files:
            grouped_files[dt['file_extension']].append(dt['file'])
        else:
            grouped_files[dt['file_extension']] = [dt['file']]
    # endregion


    # region Moving Files according to extensions to their corresponding folders
    for key,value in grouped_files.items():
        directory_name = key.split(".")[1]  ## we will make directory having extension as it's name
        if os.path.exists(directory_name):
            print('exists')
            # break
        else: 
            print('Does not exist')
            os.makedirs(directory_name)
        for asd in value:
            os.rename(asd,f'{directory_name}\\{asd}')
    # endregion

else:
    print("No folder selected")
 

asd = input('Press ENTER to exit')