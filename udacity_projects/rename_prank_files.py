import os

def rename_prank_files():

# exercice pour changer noms du folder
# step 1 - get file names from a folder
    file_list = os.listdir("/Users/xxx/prank")
    #print(file_list)
    saved_path = os.getcwd()
    print("Current Workign Directory is" + saved_path)
    os.chdir("/Users/xxx/prank")
    
# step 2 - for each file, rename filename
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)
    print(file_list)
rename_prank_files()

