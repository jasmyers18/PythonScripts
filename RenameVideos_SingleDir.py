import os, sys

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    
    if file_name.endswith('-1'):
       file_name = file_name[:-2]

    file_name = file_name.strip()
    new_name = '{}{}'.format(file_name, file_ext)

    os.rename(f, new_name)