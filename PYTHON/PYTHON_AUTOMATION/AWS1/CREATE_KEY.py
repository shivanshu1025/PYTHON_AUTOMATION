import os
def key():
 name=input("enter the name for key: ")
 path=input('''enter the path where you want to save the key locally:e.g /root/  ''')
 local=input("enter the name for key file locally ")
 os.system('''aws ec2 create-key-pair --key-name {} --output text > {}{}'''.format(name,path,local))

