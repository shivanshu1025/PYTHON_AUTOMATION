import os
def ebs():
 region=input("enter availability zone ")
 size=input("enter the size ")
 Type=input("enter the volume type ")
 os.system('''aws ec2 create-volume --volume-type {} --size {} --availability-zone {}'''.format(Type,size,region))
