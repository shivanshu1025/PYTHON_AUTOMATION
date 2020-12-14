def docker():
 while True:
  import Docker.install
  import Docker.start
  print('''1. To Install Docker On The Machine)
          2. To Start Docker Services
          3. To pull an image
          4. To Create Container
          5. To Delete Conatiner''')
  n=int(input("Choice: "))
  if n==1:
   Docker.install.install()
  elif n==2:
   Docker.start.start()
