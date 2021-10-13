import os
import shutil
path=input("Enter the name of the file to be sorted:")
listOfFiles=os.listdir(path)
for f in listOfFiles:
    name,ext=os.path.splitext(f)
    ext=ext[1:]
    if ext==" ":
        continue
    if os.path.exists(path+"/"+ext):
        shutil.move(path+"/"+f,path+"/"+ext+"/"+f)
    else:
        os.makedirs(path+"/"+ext)
        shutil.move(path+"/"+f,path+"/"+ext+"/"+f)