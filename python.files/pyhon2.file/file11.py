#Working with binary files 

fp=open("/administrator/Pictures/logo.jpeg",'rb')
file_contant=fp.read()
l=fp.name.split("/")
print("file read succesfully....")
fp.close()

fp=open(1[-1],"wb")
fp=Write(file_contant)
print("file write succesfully....")
fp.close()