import os
def launch():
  name=input("Enter Key To Attach with Instance: ")
  SG=input("Security Group for instance: ")
  image_id=input("Image ID: ")
  type=input("Instance Type: ")
  os.system('''aws ec2 run-instances --image-id {} --instance-type {} --key-name {}   --security-group-ids {}'''.format(image_id,type,name,SG))
