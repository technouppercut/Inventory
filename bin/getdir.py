#!/usr/bin/python3


import os


dirpath = os.getcwd()
print("current directory is : " + dirpath)
foldername = os.path.basename(dirpath)
print("Directory name is : " + foldername)


os.chdir("..")
dirpath = os.getcwd()
print("current directory is : " + dirpath)
foldername = os.path.basename(dirpath)
print("Directory name is : " + foldername)



updir=(os.chdir(os.path.dirname(os.getcwd())))
print(updir)

