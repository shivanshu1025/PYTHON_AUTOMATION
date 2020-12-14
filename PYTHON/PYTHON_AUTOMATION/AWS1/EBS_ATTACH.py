import os
def attach():
 I_ID=input("Enter Instance ID: ")
 V_ID=input("Enter the Volume ID: ")
 os.system('''aws ec2 attach-volume --volume-id {} --instance-id {}  --device /dev/sdb'''.format(V_ID,I_ID))  
