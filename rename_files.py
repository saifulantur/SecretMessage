import os
def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir(r"C:\Users\saifu\Downloads\udacity\prank")
    #print(file_list)
    saved_path = os.getcwd()
    #print("Current Working Directiory is " + saved_path)
    os.chdir(r"C:\Users\saifu\Downloads\udacity\prank")
    #r means row path

    #(2) for each file, rename file names
    table = str.maketrans(dict.fromkeys('0123456789'))
    for file_name in file_list:
        print("Old Name: "+file_name)
        print("New Name: "+file_name.translate(table))
        os.rename(file_name, file_name.translate(table))
    os.chdir(saved_path)
rename_files()


