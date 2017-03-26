import os, sys

for root, dirs, files in os.walk(".", topdown=True):
	for file in files:
		file_name, file_ext = os.path.splitext(file)

		if file_name.endswith('-1'):
			file_name = file_name[:-2]
			file_name = file_name.strip()

			new_name = '{}{}'.format(file_name, file_ext)

			os.rename(os.path.join(root, file), os.path.join(root, new_name))