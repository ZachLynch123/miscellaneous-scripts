import os

def rename_files():
	file_list = os.listdir(r"/Users/Zach/Downloads/prank")
	#print (file_list)
	#Get file names
	saved_path = os.getcwd()
	print("Current dir" + saved_path)
	os.chdir(r"/Users/Zach/Downloads/prank")
	for file_name in file_list:
		os.rename(file_name,file_name.translate(None,"0123456789"))
	os.chdir(saved_path)

	#rename files

rename_files()