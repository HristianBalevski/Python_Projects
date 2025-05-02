import os

directory_name = input('📁 Enter a directory name: ')

if not os.path.exists(directory_name):
    os.mkdir(directory_name)
    print(f'📂 Directory {directory_name} was created!')
else:
    print(f'📂 {directory_name} already exists!')