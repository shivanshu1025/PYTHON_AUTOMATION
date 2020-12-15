import os
def ex():
 name=input("enter name or id:  ")
 os.system("docker exec {} yum install httpd -y".format(name))
 os.system("docker exec {} /sbin/httpd".format(name))

