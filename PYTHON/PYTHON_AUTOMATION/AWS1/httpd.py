import os
def service():
 IP=input("Enter the ip address ")
 path=input("Enter the path for key ")
 os.system('''sudo ssh -i {} ec2-user@{} sudo yum install httpd -y'''.format(path,IP))
 os.system('''sudo ssh -i {} ec2-user@{} sudo systemctl start httpd'''.format(path,IP))
