import os
import LINUX
import AWS1.AWS
import Docker.main_Docker

while(True):
    print("Select One Technology: ")
    print('''1. Linux
           2. AWS
           3. Docker
           4. Exit''')
    X=int(input("Enter Your Choice: "))
    if X==1:
      LINUX.linux()

    if X==2:
       AWS1.AWS.aws()
    
    if X==3:
        Docker.main_Docker.docker()


    if X==4:
        break
























        
