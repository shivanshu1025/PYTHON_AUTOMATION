import os
import LINUX
import AWS1.AWS
import Docker.main_Docker
import LINUX.LINUX
while(True):
    print(".....................Select One Technology: .......................")
    print('''\t\t\t1. Linux
\t\t\t2. AWS
\t\t\t3. Docker
\t\t\t4. Exit''')
    X=int(input("Enter Your Choice: "))
    if X==1:
      LINUX.LINUX.linux()

    if X==2:
       AWS1.AWS.aws()
    
    if X==3:
        Docker.main_Docker.docker()


    if X==4:
        break
























        
