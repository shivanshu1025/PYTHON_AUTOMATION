import os
def cr():
 name=input("enter name for dir ")
 path=input("enter path  ")
 os.system("mkdir {}{}".format(path,name))
