"""This code copies all the files in a directory to the specified folder
   by comparing each file. If there is a another directory in the destination
   folder, it won't compare its files, only the directory.
"""   

import os
import shutil

class update:
#The folder to be copied from and to be copied to
#
#source = 'G:\\Anime'
#destination = 'K:\\Anime'

   def __init__(self, source, destination):
       self.source = source
       self.destination = destination

       base_dirs = os.listdir(source)
       destination_dirs = os.listdir(destination)

       self.base_list = []
       for dirs in base_dirs:
           self.base_list.append(dirs)

       self.destination_list = []
       for dirs in destination_dirs:
           self.destination_list.append(dirs)


   def update(self):
       #A file that stores the name of copied files
       #
       #updated_file = open('Updated anime.txt', 'w')
       updated_file = open('updates_files', 'w')

       for i in self.base_list:

           if i in self.destination_list:
               pass

           else:

               try:
                   updated_file.write(i+'\n')
                   full_file_name = os.path.join(self.source, i)
                   shutil.copytree(full_file_name, self.destination+'\\'+i)

               except:
                   updated_file.write(i+'\n')
                   full_file_name = os.path.join(self.source, i)
                   shutil.copy(full_file_name, self.destination)


if __name__ == "__main__":
   #first parameter is the source
   x = update('G:\\Anime', 'K:\\Anime')
   x.update()
