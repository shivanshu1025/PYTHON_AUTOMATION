def linux():
        while True:
            print(''' 1.  To Create Directory
                  2.  To create file
                  3.  To set permissions on file
                  4.  To delete directory/file
                  5.  To set ACL 
                  6.  To Create Group
                  7.  To change File Group ownership
                  8.  To add/change user Primary group
                  9.  To Delete User
                  10. To Install any package
                  11. To download rpm repo from internet
                  12. To remove any package
                  13. To Start Any Service
                  14. Exit''')
            x=int(input("enter The Choice: "))
            if x==1:
                name=input("enter name for dir ")
                path=input("enter path  ")
                os.system("cd {}".format(path))
                os.system("mkdir {}".format(name))
            elif x==2:
                name=input("enter name for file ")
                path=input("enter path  ")
                os.system("touch {}".format(name))
            elif x==3:
                print("""4 --> read
                     2 --> write
                     1 --> execute""")
                owner=input("Permissions for user ")
                group=input("Permissions for group ")
                other=input("Permissions for others ")
                path=input("enter path of file ")
                os.system("chmod {}{}{} {}".format(owner,group,other,path))
            elif x==4:
                name=input("Enter file name with proper path ")
                os.system("rm -rf {}".format(name))
            elif x==5:
                user=input("Enter The Username: ")
                per=input("Permission for user: ")
                file=input("Filename: ")
                os.system("setfacl -m u:{}:{} {}".format(user,per,file))
            elif x==6:
                name=input("Group Name: ")
                os.system("groupadd {}".format())
            elif x==7:
                name=input("New Group Name ")
                filename=input("Enter The File Name")
                os.system("chgrp {} {}".format(name,filename))
            elif x==8:
                name=input("Primary Group Name ")
                user=input("Enter Username ")
                os.system("usermod -g {} {}".format(name,user))
            elif x==9:
                user=input("Enter name of user to delete")
                os.system("userdel -r {}".format(user))
            elif x==10:
                pack=input("package name ")
                os.system("yum install {}".format(pack))
            elif x==11:
                url=input("enter the url ")
                os.system("wget {}".format(url))
            elif x==12:
                remove=input("Enter the package name ")
                os.system("yum remove {}".format(remove))
            elif x==13:
               service=input("Enter the Service Name ")
               os.system("systemctl start {}".format(service)) 
            elif x==14:
             break
