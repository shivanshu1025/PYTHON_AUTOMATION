def docker():
 while True:
  import Docker.install
  import Docker.start
  import Docker.PULL
  import Docker.Cr_Container
  import Docker.DEL
  import Docker.EX
  print('''1. To Install Docker On The Machine
2. To Start Docker Services
3. To pull an image
4. To Create Container
5. To Delete Conatiner
6. To Install HTTPD services inside container
7. EXIT''')
  n=int(input("Choice: "))
  if n==1:
   Docker.install.install()
  elif n==2:
   Docker.start.start()
  elif n==3:
   Docker.PULL.pull()
  elif n==4:
   Docker.Cr_Container.cont()
  elif n==5:
   Docker.DEL.del1()
  elif n==6:
   Docker.EX.ex()
  elif n==7:
   break
