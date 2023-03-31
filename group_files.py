import os
file_details = [{'file': 'another_sample_text.txt', 'file_path': 'C:\\Users\\yogesh\\Desktop\\temp\\segregator_try\\another_sample_text.txt', 'file_extension': '.txt', 'file_size': 0, 'created_time': 1679896587.128361, 'modified_time': 1679896587.2069356}, {'file': 'hello.java', 'file_path': 'C:\\Users\\yogesh\\Desktop\\temp\\segregator_try\\hello.java', 'file_extension': '.java', 'file_size': 0, 'created_time': 1679896553.6397345, 'modified_time': 1679896553.7650256}, {'file': 'hello.py', 'file_path': 'C:\\Users\\yogesh\\Desktop\\temp\\segregator_try\\hello.py', 'file_extension': '.py', 'file_size': 0, 'created_time': 1679896557.172851, 'modified_time': 1679896557.2669435}, {'file': 'index.html', 'file_path': 'C:\\Users\\yogesh\\Desktop\\temp\\segregator_try\\index.html', 'file_extension': '.html', 'file_size': 54864, 'created_time': 1679896505.3754022, 'modified_time': 1678433899.4579868}, {'file': 'sample_text.txt', 'file_path': 'C:\\Users\\yogesh\\Desktop\\temp\\segregator_try\\sample_text.txt', 'file_extension': '.txt', 'file_size': 21, 'created_time': 1679896578.4570484, 'modified_time': 1679896578.5198781}, {'file': 'style.css', 'file_path': 'C:\\Users\\yogesh\\Desktop\\temp\\segregator_try\\style.css', 'file_extension': '.css', 'file_size': 23, 'created_time': 1679896543.497603, 'modified_time': 1679896543.588218}]

grouped_files = {}
for dt in file_details:
    if dt['file_extension'] in grouped_files:
        grouped_files[dt['file_extension']].append(dt['file'])
    else:
        grouped_files[dt['file_extension']] = [dt['file']]
# print(grouped_files)

for key,value in grouped_files.items():
    directory_name = key.split(".")[1]  ## we will make directory having extension as it's name

    if os.path.exists(key):
        print('if')
        pass

    else:
        print('else')
        os.makedirs(key)

    for i in grouped_files[key]:
        print("  ",i)
    print()


