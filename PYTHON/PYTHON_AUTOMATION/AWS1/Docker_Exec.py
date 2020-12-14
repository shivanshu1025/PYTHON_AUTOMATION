import os
def ex():
 IP=input("Enter the ip address ")
 path=input("Enter the path for key ")
 expose=input("Enter Port NO. ")
 os.system('''sudo ssh -i {} ec2-user@{} sudo docker run -itd -p {}:80  --name myos centos'''.format(path,IP,expose))
 os.system(''' sudo ssh -i {} ec2-user@{} sudo docker exec myos usr/sbin/httpd'''.format(path,IP))    
