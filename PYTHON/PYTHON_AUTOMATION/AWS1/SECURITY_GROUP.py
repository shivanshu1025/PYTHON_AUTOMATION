import os
def sg():
  name_SG=input("Please enter Name For Security Group: ")
  desc=input("DESCRIPTION : ")
  os.system("aws ec2 create-security-group --group-name {} --description {}".format(name_SG,desc))
