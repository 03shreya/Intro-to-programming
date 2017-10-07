import os
def rename_files():
    # get file names from a folder
    file_list = os.listdir(r"C:\Users\shreya\Downloads\ipnd-starter-code-master (1).zip\ipnd-starter-code-master\stage_3\lesson_3.2_using_functions\secret_message\prank")
    print (file_list)
    for filename in file_list:
        os.rename(filename, filename.translate(None,"0123456789"))
        
