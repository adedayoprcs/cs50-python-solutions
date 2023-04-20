#Access the files on my phone or my computer. 
import os
import shutil
entries = os.listdir(r"C:\Users\Precious pc\Pictures\Saved Pictures")
print(entries)

for picture in entries:
    if "png" in picture:
        file, extension = picture.split(".")
        rename_file = file.replace("1665824933465","Torima")
        print(rename_file)
        
        







#check the name of the file or the extension, and replace it with torima 1 - end. 
#which means I need a loop. 



#for picture in pictures, if picture ends with ... replace("torima ")