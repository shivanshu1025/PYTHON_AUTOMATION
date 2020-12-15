import os 
def cont():
 name=input("enter the name for container ")
 port=input("Port you want to expose ")
 port1=input("Enter Mapping port no.  ")
 image=input("image ")
 os.system('''docker run -itd -p {}:{} --name {} {}'''.format(port1,port,name,image))
