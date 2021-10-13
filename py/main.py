import os
os.mkdir("/WhiteHat Junior/Class 99/newFolder")
os.getcwd()
path="/WhiteHat Junior/Class 99/main.py"
pathExists=os.path.exists(path)
print(pathExists)
root_ext=os.path.splitext(path)
print("root part",root_ext[0])
print("extension part",root_ext[1])
os.listdir()