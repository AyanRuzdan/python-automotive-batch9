import os

from logger import write_file_log

def create_project(name):
    
    #list of folders to be made
    folders = ['folder1', 'f_automotive', 'folder_electric']
    
    # os.makedirs makes the New Folder
    os.makedirs(name, exist_ok=True)
    
    # join file paths so that it is readable
    logs = os.path.join(name, 'file_log.txt')
    
    # pick each folder from the list
    # create folder path that is system readable
    # make directories accordingly
    # write to log
    for folder in folders:
        folder_path = os.path.join(name, folder)
        os.makedirs(folder_path, exist_ok=True)
        write_file_log(logs, f"Folder created: {folder_path}")
    
    
create_project("My New Folder")