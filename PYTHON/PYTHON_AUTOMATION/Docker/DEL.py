import os 
def del1():
    name=input("Enter name or id ")
    os.system("docker rm -f {}".format(name))
