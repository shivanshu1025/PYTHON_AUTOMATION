import os
def pull():
 name=input("Enter the image name")
 os.system("docker pull {}".format(name))
