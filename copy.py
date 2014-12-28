"""This code copies all the files in a directory to the specified folder
   by comparing each file. If there is a another directory in the destination
   folder, it won't compare its files, only the directory.
"""   

import os
import shutil

#The folder to be copied to
destination_dir = 'K:\\Anime'

#The folder to be copied from
basedir = 'G:\\Anime'

#A file that gives the name of copied files
updated_anime = open('Updated anime.txt', 'w')

base_dirs = os.listdir(basedir)
destination_dirs = os.listdir(destination_dir)

base_list = []
for dirs in base_dirs:
    base_list.append(dirs)

destination_list = []
for dirs in destination_dirs:
    destination_list.append(dirs)


#actual copying
for i in base_list:
    if i in destination_dirs:
        pass
    else:
        try:
            updated_anime.write(i+'\n')
            full_file_name = os.path.join(basedir, i)
            shutil.copytree(full_file_name, destination_dir+'\\'+i)
        except:
            updated_anime.write(i+'\n')
            full_file_name = os.path.join(basedir, i)
            shutil.copy(full_file_name, destination_dir)
            

            

