# imports
from directory_creator import create_project

# list of folders to be made
folders = ['folder1', 'f_automotive', 'folder_electric',
               'lv1/lv2', 'outer/inner/innermost']

# call directory creation function
create_project(folders, "My New Folder")
