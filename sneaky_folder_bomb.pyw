import os

#Adds the directory to the desktop
desktop=os.path.join(os.path.expanduser("~"),"Desktop")

i=1
while True:
    new_dir='Spamming'+str(i) #Folder name Spamming1, Spamming2, and so on
    dir_path=os.path.join(desktop,new_dir)
    os.mkdir(dir_path)
    i+=1